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


def configure_mail_sender(env):
    smtp_user = get_smtp_config()["smtp_user"]
    if not smtp_user:
        return

    params = env["ir.config_parameter"].sudo()
    params.set_param("mail.default.from", smtp_user)
    params.set_param("mail.catchall.domain", smtp_user.rsplit("@", 1)[-1])

    for company in env["res.company"].sudo().search([]):
        if not company.email:
            company.email = smtp_user

    template = env.ref("auth_signup.set_password_email", raise_if_not_found=False)
    if template:
        template.sudo().write({"email_from": smtp_user})