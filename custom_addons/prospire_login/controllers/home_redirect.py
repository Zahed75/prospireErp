from odoo import http
from odoo.http import request

from odoo.addons.website.controllers.main import Website


class ProspireWebsiteHome(Website):
    """Send visitors landing on / straight to the branded login screen."""

    @http.route()
    def index(self, **kw):
        if request.session.uid:
            return request.redirect('/web')
        return request.redirect('/web/login')
