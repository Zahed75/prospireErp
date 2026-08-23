import os

from odoo import models, fields, api
from datetime import datetime

class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def _register_hook(self):
        """Force database expiration to 2099 on every registry load."""
        res = super()._register_hook()
        self.set_param('database.expiration_date', '2126-12-31 23:59:59')
        # Also remove any enterprise registration warning
        self.set_param('database.enterprise_code', 'SURRENDER-TO-SYCO')
        # Enforce production base URL so invitation emails use the real domain
        base_url = os.environ.get('BASE_URL', 'https://hq.prospirenext.com')
        self.set_param('web.base.url', base_url)
        self.set_param('web.base.url.freeze', '1')
        # Keep user sessions alive for 30 days instead of the 7-day default
        self.set_param('sessions.max_inactivity_seconds', '2592000')
        # Real domain for bounce/reply-to addresses — improves deliverability
        # (container-hostname addresses are a spam signal)
        website_domain = os.environ.get('WEBSITE_DOMAIN', 'hq.prospirenext.com')
        self.set_param('mail.catchall.domain', website_domain)
        return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('key') == 'database.expiration_date':
                vals['value'] = '2126-12-31 23:59:59'
        return super().create(vals_list)

    def write(self, vals):
        if vals.get('key') == 'database.expiration_date':
            vals['value'] = '2126-12-31 23:59:59'
        return super().write(vals)

class PublisherWarrantyContract(models.AbstractModel):
    _inherit = 'publisher_warranty.contract'

    @api.model
    def _get_sys_logs(self):
        """Disable phone-home to Odoo servers for subscription checks."""
        return {"messages": [], "enterprise_info": {}}

    def update_notification(self, cron_mode=True):
        """Silence subscription notifications."""
        return True
