import os

from odoo import models
from odoo.http import request

VEXA_DOMAIN = os.environ.get("VEXA_DOMAIN", "hq.vexanext.com")


def _request_host():
    try:
        return request.httprequest.host.split(":")[0]
    except RuntimeError:  # outside of a request context
        return ""


def _get_vexa_company(env):
    return env["res.company"].sudo().search([("name", "ilike", "vexanext")], limit=1)


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        result = super().session_info()
        if _request_host() != VEXA_DOMAIN or not request.session.uid:
            return result
        vexa = _get_vexa_company(self.env)
        companies = (result.get("user_companies") or {}).get("allowed_companies") or {}
        if not vexa or vexa.id not in companies:
            return result
        # Company switcher offers only VexaNext on this domain
        result["user_companies"]["allowed_companies"] = {vexa.id: companies[vexa.id]}
        result["user_companies"]["current_company"] = vexa.id
        result["user_companies"]["disallowed_ancestor_companies"] = {}
        return result

    @classmethod
    def _dispatch(cls, endpoint):
        if _request_host() == VEXA_DOMAIN and request.session.uid:
            vexa = _get_vexa_company(request.env)
            if vexa and vexa.id in request.env.user.company_ids.ids:
                # Server-side enforcement: ignore the client-sent cids cookie
                # and scope every request on this domain to VexaNext.
                request.update_env(
                    context=dict(request.env.context, allowed_company_ids=[vexa.id])
                )
        return super()._dispatch(endpoint)
