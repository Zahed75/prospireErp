import os


def get_smtp_config():
    """Return SMTP settings in the form expected by ir.mail_server."""
    smtp_user = os.environ.get("SMTP_USER", "").strip()
    # Gmail displays app passwords in four-character groups, but SMTP AUTH
    # expects the 16-character value without separators.
    smtp_password = "".join(os.environ.get("SMTP_PASSWORD", "").split())
    return {
        "smtp_host": os.environ.get("SMTP_HOST", "smtp.gmail.com").strip(),
        "smtp_port": int(os.environ.get("SMTP_PORT", "587")),
        "smtp_authentication": "login",
        "smtp_user": smtp_user,
        "smtp_pass": smtp_password,
        "smtp_encryption": os.environ.get("SMTP_ENCRYPTION", "starttls").strip(),
        "from_filter": smtp_user,
    }


def get_vexa_smtp_config():
    """SMTP settings for the VexaNext company sender, or None if not configured."""
    vexa_user = os.environ.get("VEXA_SMTP_USER", "").strip()
    if not vexa_user:
        return None
    return {
        "name": "Vexa SMTP",
        "smtp_host": os.environ.get("VEXA_SMTP_HOST", "smtp.gmail.com").strip(),
        "smtp_port": int(os.environ.get("VEXA_SMTP_PORT", "587")),
        "smtp_authentication": "login",
        "smtp_user": vexa_user,
        "smtp_pass": "".join(os.environ.get("VEXA_SMTP_PASSWORD", "").split()),
        "smtp_encryption": os.environ.get("VEXA_SMTP_ENCRYPTION", "starttls").strip(),
        "from_filter": vexa_user,
        "sequence": 5,
        "active": True,
    }


def configure_mail_sender(env):
    smtp_user = get_smtp_config()["smtp_user"]
    if not smtp_user:
        return

    params = env["ir.config_parameter"].sudo()
    params.set_param("mail.default.from", smtp_user)
    # Never a public provider (gmail.com) or the website domain: the Reply-To
    # alias <alias>@domain must be a mailbox that actually exists. Empty means
    # Odoo replies go to the sender — right for a Gmail-SMTP deployment.
    params.set_param("mail.catchall.domain", os.environ.get("MAIL_CATCHALL_DOMAIN", "").strip())

    for company in env["res.company"].sudo().search([]):
        # VexaNext companies get the Vexa sender, not the Prospire one
        if not company.email and "vexanext" not in company.name.lower():
            company.email = smtp_user

    template = env.ref("auth_signup.set_password_email", raise_if_not_found=False)
    if template:
        template.sudo().write({"email_from": smtp_user})


def configure_vexa_mail_server(env):
    """Create/update the Vexa SMTP server and disable conflicting duplicates.

    Odoo routes each outgoing message through the server whose From Filtering
    matches the message From address. A server with an EMPTY from_filter
    matches EVERYTHING, so leftover manually-created servers for the same
    account must be deactivated or they hijack unrelated mail.
    """
    values = get_vexa_smtp_config()
    if not values:
        return
    Smtp = env["ir.mail_server"].sudo()
    existing = Smtp.search(
        ["|", ("name", "=", "Vexa SMTP"), ("smtp_user", "=", values["smtp_user"])],
        limit=1,
    )
    if existing:
        existing.write(values)
        server = existing
    else:
        server = Smtp.create(values)
    # Deactivate other servers on the same account (e.g. a manual entry with
    # an empty from_filter that would catch all outgoing mail).
    duplicates = Smtp.search([("smtp_user", "=", values["smtp_user"]), ("id", "!=", server.id)])
    if duplicates:
        duplicates.write({"active": False})
    company = env["res.company"].sudo().search([("name", "ilike", "vexanext")], limit=1)
    if company:
        company.write({"email": values["smtp_user"]})
