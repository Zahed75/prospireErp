# -*- coding: utf-8 -*-
import logging

from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.home import Home
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

_logger = logging.getLogger(__name__)

COUPON_PARAM = 'prospire.course.coupon'


class Home(Home):
    """Same class name as web's Home: Odoo merges the controller extensions."""

    @http.route()
    def login_successful_external_user(self, **kwargs):
        # Students (portal/public users) go straight to the course catalog
        # instead of the generic landing page; internal users keep the
        # standard behavior (the /odoo backend).
        if not request.env.user._is_internal():
            return request.redirect('/slides')
        return super().login_successful_external_user(**kwargs)


class AuthSignupHome(AuthSignupHome):
    """Force newly-signed-up learners to land on /slides."""

    @http.route()
    def web_auth_signup(self, *args, **kw):
        # Make sure the signup form always carries a redirect back to the
        # course catalog. This covers direct /web/signup visits and any
        # signup link that does not already include ?redirect=/slides.
        if not kw.get('redirect') and not request.params.get('redirect'):
            kw['redirect'] = '/slides'
            request.params['redirect'] = '/slides'
        return super().web_auth_signup(*args, **kw)


class ProspireSlidesController(http.Controller):

    @http.route('/slides/coupon_join', type='jsonrpc', auth='user', website=True)
    def slides_coupon_join(self, channel_id, coupon):
        """Enroll the current user into an invite-only course with a coupon."""
        channel = request.env['slide.channel'].sudo().browse(channel_id).exists()
        if not channel:
            return {'success': False, 'error': 'Course not found'}
        expected = request.env['ir.config_parameter'].sudo().get_param(COUPON_PARAM)
        if not expected or (coupon or '').strip() != expected:
            return {'success': False, 'error': 'Invalid coupon code'}
        channel._action_add_members(request.env.user.partner_id)
        _logger.info(
            'prospire_elearning: user %s enrolled into course %r via coupon',
            request.env.user.login, channel.name,
        )
        return {'success': True}
