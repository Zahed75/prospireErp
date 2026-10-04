from odoo import api, models
from odoo.tools import formataddr


class MailMessage(models.Model):
    _inherit = "mail.message"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("model") and vals.get("res_id") and not vals.get("email_from"):
                company = self._brand_company(vals["model"], vals["res_id"])
                if company and company.email:
                    vals["email_from"] = formataddr((company.name, company.email))
        return super().create(vals_list)

    @api.model
    def _brand_company(self, model, res_id):
        try:
            record = self.env[model].browse(int(res_id)).exists()
        except Exception:
            return self.env["res.company"]
        if not record or "company_id" not in record._fields:
            return self.env["res.company"]
        return record.company_id
