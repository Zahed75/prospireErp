import logging

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Light branding setup after install.

    Ensures the website has a name and falls back to the company logo when
    no website logo is set. Never overwrites an existing logo, and never
    raises: a failure here must not break the boot/update cycle.
    """
    try:
        Website = env['website'].sudo()
        for website in Website.search([]):
            values = {}
            if not website.name:
                values['name'] = website.company_id.name or 'ProspireNext'
            if not website.logo and website.company_id.logo:
                values['logo'] = website.company_id.logo
            if values:
                website.write(values)
                _logger.info(
                    'prospire_elearning: updated website %s with %s',
                    website.id, sorted(values),
                )
    except Exception:
        _logger.exception(
            'prospire_elearning: post-init website branding skipped due to an error'
        )
