# -*- coding: utf-8 -*-
import logging

from odoo import models

_logger = logging.getLogger(__name__)

TRAINER_LOGIN = 'zahed.hasan.rabbi@gmail.com'
AUTO_PORTAL_PARAM = 'prospire.auto_portal'
# uid 1 = OdooBot (superuser), uid 2 = base.user_admin
PROTECTED_UIDS = (1, 2)


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _prospire_demote_plain_users(self):
        """Demote "plain" internal users to portal, once per boot sync.

        A plain internal user is an active res.users with share=False whose
        only group is base.group_user (nothing else). Students must never
        land on the /odoo backend. Superuser/admin and the course trainer
        are always skipped.

        Escape hatch: set ir.config_parameter 'prospire.auto_portal' to '0'
        to disable entirely. Never raises: the caller logs and continues.
        """
        try:
            ICP = self.env['ir.config_parameter'].sudo()
            if ICP.get_param(AUTO_PORTAL_PARAM) == '0':
                _logger.info(
                    'prospire_elearning: auto-portal disabled via %s=0, skipping',
                    AUTO_PORTAL_PARAM,
                )
                return
            group_user = self.env.ref('base.group_user')
            group_portal = self.env.ref('base.group_portal')
            trainer = self.search([('login', '=', TRAINER_LOGIN)], limit=1)
            candidates = self.search([
                ('share', '=', False),
                ('active', '=', True),
            ])
            for user in candidates:
                if user.id in PROTECTED_UIDS or (trainer and user.id == trainer.id):
                    continue
                if len(user.groups_id) != 1 or user.groups_id.id != group_user.id:
                    continue
                user.write({'groups_id': [(3, group_user.id), (4, group_portal.id)]})
                _logger.info(
                    'prospire_elearning: demoted plain internal user %r (login=%s) to portal',
                    user.name, user.login,
                )
        except Exception:
            _logger.exception(
                'prospire_elearning: auto-portal demotion failed, skipping'
            )
