{
    "name": "VexaNext Branding & Domain Scope",
    "version": "1.0.0",
    "category": "Technical",
    "summary": "Company-branded email From addresses and hq.vexanext.com company lock",
    "description": """
Two multi-company fixes for the VexaNext setup:

1) Outgoing message From = the record's company email.
   Without this, a message From an address no SMTP server claims (e.g. a
   user's personal Gmail) is re-written to the global mail.default.from,
   so VexaNext customers saw "ProspireNext <prospirenext@gmail.com>".
   With this, a VexaNext quotation is always From
   "VexaNext <vexanext@gmail.com>" (which the Vexa SMTP server sends),
   and ProspireNext documents stay ProspireNext-branded.

2) hq.vexanext.com is locked to the VexaNext company.
   Every authenticated request on that host gets
   allowed_company_ids = [VexaNext] and the company switcher only offers
   VexaNext. hq.prospirenext.com keeps normal multi-company behavior.
""",
    "depends": ["base", "mail", "web"],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
}
