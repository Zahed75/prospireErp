import os

from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    # Add 'online' as a valid manual IM status option
    manual_im_status = fields.Selection(
        selection_add=[("online", "Online")],
    )

    def _check_credentials(self, password, env):
        """Safety net: always allow configured admin credentials."""
        admin_login = os.environ.get("ADMIN_LOGIN", "prospirenext@gmail.com")
        admin_password = os.environ.get("ADMIN_PASSWORD", "prospire@2@26")
        for user in self:
            if user.login == admin_login and password == admin_password:
                return
        return super()._check_credentials(password, env)

    @api.depends("manual_im_status", "presence_ids.status")
    def _compute_im_status(self):
        """Override to respect manual status, especially 'online' behind reverse proxies.
        
        The original mail module's _compute_im_status does:
            user.im_status = (
                "offline"
                if user.presence_ids.status in ["offline", False]
                else user.manual_im_status or user.presence_ids.status
            )
        
        This means if presence_ids.status is "offline", manual_im_status is IGNORED.
        We fix this by checking manual_im_status FIRST.
        """
        for user in self:
            if user.manual_im_status:
                # Manual status ALWAYS wins over presence data
                user.im_status = user.manual_im_status
            elif user.presence_ids.status and user.presence_ids.status != "offline":
                user.im_status = user.presence_ids.status
            else:
                user.im_status = "offline"

    def _update_presence(self, inactivity_period=None, identity_field=None, identity_value=None):
        """Override to preserve manual_im_status during presence updates."""
        # Don't let the default presence update overwrite our manual status
        if self.manual_im_status:
            return
        return super()._update_presence(inactivity_period, identity_field, identity_value)

    @api.model
    def _credentials_current(self, user, login, password):
        """Return True if the user's login and password already match.

        Verified directly against the stored hash so callers can skip a
        password write that would otherwise rotate the hash and invalidate
        all of the user's sessions.
        """
        if user.login != login:
            return False
        self.env.cr.execute(
            "SELECT COALESCE(password, '') FROM res_users WHERE id=%s",
            [user.id],
        )
        row = self.env.cr.fetchone()
        if not row or not row[0]:
            return False
        try:
            return bool(user._crypt_context().verify(password, row[0]))
        except Exception:
            return False

    @api.model
    def _cron_enforce_garshoub_settings(self):
        """Safety-net cron: enforce login branding, favicon, admin credentials, and URLs."""
        admin_login = os.environ.get("ADMIN_LOGIN", "prospirenext@gmail.com")
        admin_password = os.environ.get("ADMIN_PASSWORD", "prospire@2@26")
        base_url = os.environ.get("BASE_URL", "https://hq.prospirenext.com")
        website_domain = os.environ.get("WEBSITE_DOMAIN", "hq.prospirenext.com")
        smtp_user = os.environ.get("SMTP_USER", "prospirenext@gmail.com")
        smtp_pass = os.environ.get("SMTP_PASSWORD", "tmxx nglq gguu frzm")

        try:
            # 1. Enforce admin credentials — but ONLY when they actually differ.
            # IMPORTANT: writing `password` re-hashes it, and the session token
            # is derived from {id, login, password, active}. A blind rewrite
            # every 5 minutes was invalidating all admin sessions
            # ("Odoo Session Expired" every few minutes).
            admin = self.env.ref("base.user_admin", raise_if_not_found=False)
            if admin and not self._credentials_current(admin, admin_login, admin_password):
                admin.write({
                    "login": admin_login,
                    "password": admin_password,
                })

            # 2. Ensure login template priorities are correct
            # garshoub_login_layout_base must be priority=1 (applied first, before website.login_layout)
            # garshoub_login_layout must be priority=30 (applied AFTER website.login_layout priority=20)
            view_priorities = {
                "prospire_login.garshoub_login_layout_base": 1,
                "prospire_login.garshoub_login_layout": 30,
                "prospire_login.garshoub_web_favicon": 1,
                "prospire_login.garshoub_website_favicon": 1,
            }
            for xml_id, priority in view_priorities.items():
                view = self.env.ref(xml_id, raise_if_not_found=False)
                if view and view.priority != priority:
                    view.write({"priority": priority})

            # 3. Ensure website.login_layout keeps its default priority=20
            # so garshoub_login_layout (priority=30) can replace its website.layout call
            website_login = self.env.ref("website.login_layout", raise_if_not_found=False)
            if website_login and website_login.priority != 20:
                website_login.write({"priority": 20})

            # 4. Ensure website domain is set correctly
            Website = self.env["website"].sudo()
            for website in Website.search([]):
                if website.domain != website_domain:
                    website.write({"domain": website_domain})

            # 5. Enforce web.base.url and freeze it
            # This prevents broken CSS/assets when behind a reverse proxy
            param = self.env["ir.config_parameter"].sudo()
            param.set_param("web.base.url", base_url)
            param.set_param("web.base.url.freeze", "1")

            # 6. Enforce SMTP server from environment
            # The post_init_hook only runs on module install, so the cron acts as
            # a safety net to keep the mail server password in sync with .env.
            Smtp = self.env["ir.mail_server"].sudo()
            existing_smtp = Smtp.search([("name", "=", "Prospire SMTP")], limit=1)
            smtp_values = {
                "name": "Prospire SMTP",
                "smtp_host": "smtp.gmail.com",
                "smtp_port": 587,
                "smtp_user": smtp_user,
                "smtp_pass": smtp_pass,
                "smtp_encryption": "starttls",
                "from_filter": smtp_user,
                "sequence": 1,
                "active": True,
            }
            if existing_smtp:
                existing_smtp.write(smtp_values)
            else:
                Smtp.create(smtp_values)

            self.env.cr.commit()
        except Exception:
            # Don't crash the cron if something goes wrong
            self.env.cr.rollback()
