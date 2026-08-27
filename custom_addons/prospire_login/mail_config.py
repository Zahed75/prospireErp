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