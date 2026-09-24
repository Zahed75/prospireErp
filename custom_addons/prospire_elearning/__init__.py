# -*- coding: utf-8 -*-
import base64
import json
import logging
import os

from .course_content import (
    CHANNEL_DESCRIPTION,
    CHANNEL_DESCRIPTION_HTML,
    CHANNEL_DESCRIPTION_SHORT,
    CURRICULUM,
)

from . import controllers  # noqa: F401
from . import models  # noqa: F401

_logger = logging.getLogger(__name__)

TARGET_CHANNEL_NAME = 'Odoo Technical Training SDTek'
LEGACY_CHANNEL_NAME = 'SDTEKH — Odoo Technical Training'
HANDBOOK_SECTION_NAME = 'Course Orientation'
HANDBOOK_SLIDE_NAME = 'Technical Orientation — Course Handbook'
COUPON_PARAM = 'prospire.course.coupon'
COUPON_CODE = 'SD@2026'
COMPANY_PHONE = '+880 16118 14937'
HANDBOOK_SLIDE_SUMMARY = (
    'Level: Beginner | Duration: ~0.5h. Download the course handbook (PDF): '
    'curriculum overview, setup checklists and reference material for the full track.'
)
HANDBOOK_PDF_RELPATH = os.path.join('static', 'src', 'pdf', 'OdooTechnical.pdf')
COVER_IMAGE_RELPATH = os.path.join('static', 'src', 'img', 'course_cover.png')
TRAINER_LOGIN = 'zahed.hasan.rabbi@gmail.com'

# Every name the curriculum owns; anything else under the target channel is
# sample/demo content and gets archived (never unlinked).
CURRICULUM_NAMES = {HANDBOOK_SECTION_NAME, HANDBOOK_SLIDE_NAME}
for _section in CURRICULUM:
    CURRICULUM_NAMES.add(_section['name'])
    for _lesson in _section['lessons']:
        CURRICULUM_NAMES.add(_lesson['name'])

# Sections whose lessons are free preview (accessible without joining):
# the orientation plus the first two curriculum sections. Applied only on
# the creation path — existing slides are never touched.
PREVIEW_SECTION_NAMES = {
    HANDBOOK_SECTION_NAME,
    CURRICULUM[0]['name'],
    CURRICULUM[1]['name'],
}


def post_init_hook(env):
    try:
        _setup_website_branding(env)
    except Exception:
        _logger.exception(
            'prospire_elearning: post-init website branding skipped due to an error'
        )
    try:
        _setup_course(env)
    except Exception:
        _logger.exception(
            'prospire_elearning: post-init course setup skipped due to an error'
        )
    try:
        # Runs on every boot by design; escape hatch via the
        # 'prospire.auto_portal' config parameter (see models/res_users.py).
        env['res.users'].sudo()._prospire_demote_plain_users()
    except Exception:
        _logger.exception(
            'prospire_elearning: post-init auto-portal demotion skipped due to an error'
        )


def _setup_website_branding(env):
    """Branding setup: website name, logo and company phone.

    The logo is ALWAYS overwritten with the company logo (the current
    placeholder is the stock "Your Logo"). The company email is left alone:
    it doubles as the SMTP sender identity.
    """
    Website = env['website'].sudo()
    for website in Website.search([]):
        values = {}
        if not website.name:
            values['name'] = website.company_id.name or 'ProspireNext'
        if website.company_id.logo and website.logo != website.company_id.logo:
            values['logo'] = website.company_id.logo
        company = website.company_id
        if company.phone != COMPANY_PHONE:
            company.phone = COMPANY_PHONE
            _logger.info(
                'prospire_elearning: company %s phone set to %s',
                company.id, COMPANY_PHONE,
            )
        if values:
            website.write(values)
            _logger.info(
                'prospire_elearning: updated website %s with %s',
                website.id, sorted(values),
            )


def _get_or_create_tag(Tag, name):
    tag = Tag.search([('name', '=', name)], limit=1)
    if not tag:
        tag = Tag.create({'name': name})
        _logger.info('prospire_elearning: created slide tag %r', name)
    return tag


def _resolve_target_channel(Channel, env):
    """(a) find the existing course channel, (b) create it when missing."""
    channel = Channel.search([('name', '=', TARGET_CHANNEL_NAME)], limit=1)
    if channel:
        _logger.info(
            'prospire_elearning: using existing channel %r (id=%s)',
            channel.name, channel.id,
        )
        return channel
    handbook_line = (
        '<p><strong>Start here:</strong> download the "Technical Orientation '
        '— Course Handbook" (PDF) in the Course Orientation section below.</p>'
    )
    channel = Channel.create({
        'name': TARGET_CHANNEL_NAME,
        'channel_type': 'training',
        'visibility': 'public',
        'enroll': 'public',
        'is_published': True,
        'allow_comment': True,
        'user_id': env.ref('base.user_admin').id,
        'description_short': CHANNEL_DESCRIPTION_SHORT,
        'description': handbook_line + CHANNEL_DESCRIPTION,
        'description_html': CHANNEL_DESCRIPTION_HTML,
    })
    _logger.info(
        'prospire_elearning: created channel %r (id=%s)',
        channel.name, channel.id,
    )
    return channel


def _apply_channel_branding(env, channel):
    """Refresh course cover, access policy, trainer and description on every sync."""
    values = {
        'description_short': CHANNEL_DESCRIPTION_SHORT,
        'description': CHANNEL_DESCRIPTION,
        'description_html': CHANNEL_DESCRIPTION_HTML,
        # Paid course: only members see content; joining requires an
        # invitation or a coupon (see /slides/coupon_join).
        'visibility': 'members',
        'enroll': 'invite',
    }
    env['ir.config_parameter'].sudo().set_param(COUPON_PARAM, COUPON_CODE)
    cover_path = os.path.join(os.path.dirname(__file__), COVER_IMAGE_RELPATH)
    try:
        with open(cover_path, 'rb') as cover_file:
            values['image_1920'] = base64.b64encode(cover_file.read())
    except Exception:
        _logger.warning(
            'prospire_elearning: course cover missing or unreadable at %s',
            cover_path, exc_info=True,
        )
    trainer = env['res.users'].sudo().search(
        [('login', '=', TRAINER_LOGIN)], limit=1,
    )
    if trainer:
        values['user_id'] = trainer.id
    # The course header background comes from cover_properties, not from
    # image_1920: stock slides channels hardcode a purple gradient there.
    # Point the background-image at the channel cover and neutralize the
    # purple so our dark banner shows full-width.
    try:
        props = json.loads(channel.cover_properties) if channel.cover_properties else {}
    except ValueError:
        props = {}
    props['background-image'] = 'url(/web/image/slide.channel/%s/image_1920)' % channel.id
    props['background_color_style'] = 'background-color: #0D0B1E; background-image: none;'
    props['opacity'] = '0'
    values['cover_properties'] = json.dumps(props)
    channel.write(values)
    _logger.info(
        'prospire_elearning: channel %r branding refreshed (cover=%s, trainer=%s)',
        channel.name, 'image_1920' in values, trainer.login if trainer else 'not found',
    )


def _archive_legacy_channel(env, Channel, Slide, target):
    """Archive the duplicate channel created by the first XML-data deploy."""
    legacy = Channel.with_context(active_test=False).search(
        [('name', '=', LEGACY_CHANNEL_NAME)], limit=1,
    )
    if not legacy or legacy.id == target.id:
        return
    slides = Slide.with_context(active_test=False).search([
        ('channel_id', '=', legacy.id),
    ])
    slide_count = len(slides)
    slides.write({'active': False})
    legacy.write({'active': False, 'is_published': False})
    _logger.info(
        'prospire_elearning: archived legacy channel %r (id=%s): %s slide(s) '
        'deactivated, channel deactivated and unpublished',
        legacy.name, legacy.id, slide_count,
    )


def _archive_sample_slides(Slide, channel):
    """Archive (active=False, never unlink) non-curriculum slides."""
    existing = Slide.with_context(active_test=False).search([
        ('channel_id', '=', channel.id),
    ])
    samples = existing.filtered(lambda slide: slide.name not in CURRICULUM_NAMES)
    for slide in samples:
        _logger.info(
            'prospire_elearning: archiving sample slide %r (id=%s) on channel %r',
            slide.name, slide.id, channel.name,
        )
    samples.write({'active': False})
    return existing


def _create_orientation(Slide, channel, seq):
    """Course Orientation section with the handbook PDF slide."""
    if Slide.with_context(active_test=False).search([
        ('channel_id', '=', channel.id),
        ('name', '=', HANDBOOK_SECTION_NAME),
        ('is_category', '=', True),
    ], limit=1):
        return seq
    section = Slide.create({
        'name': HANDBOOK_SECTION_NAME,
        'is_category': True,
        'channel_id': channel.id,
        'sequence': seq + 1,
    })
    seq += 1
    handbook_values = {
        'name': HANDBOOK_SLIDE_NAME,
        'channel_id': channel.id,
        'category_id': section.id,
        'sequence': seq + 1,
        'slide_category': 'document',
        'is_published': True,
        'is_preview': True,
        'completion_time': 0.5,
        'description': HANDBOOK_SLIDE_SUMMARY,
    }
    pdf_path = os.path.join(os.path.dirname(__file__), HANDBOOK_PDF_RELPATH)
    try:
        with open(pdf_path, 'rb') as pdf_file:
            handbook_values['binary_content'] = base64.b64encode(pdf_file.read())
    except Exception:
        _logger.warning(
            'prospire_elearning: handbook PDF missing or unreadable at %s; '
            'creating the orientation slide without the file',
            pdf_path, exc_info=True,
        )
    Slide.create(handbook_values)
    _logger.info(
        'prospire_elearning: created orientation section + handbook slide on channel %r',
        channel.name,
    )
    return seq + 1


def _create_curriculum(Slide, channel, tags, seq, existing):
    """Create missing sections and lessons; skip sections that already exist."""
    existing_sections = {
        slide.name: slide
        for slide in existing
        if slide.is_category and slide.active
    }
    created_sections = 0
    created_lessons = 0
    for section_data in CURRICULUM:
        if section_data['name'] in existing_sections:
            continue
        seq += 1
        section = Slide.create({
            'name': section_data['name'],
            'is_category': True,
            'channel_id': channel.id,
            'sequence': seq,
        })
        created_sections += 1
        for lesson_data in section_data['lessons']:
            seq += 1
            Slide.create({
                'name': lesson_data['name'],
                'channel_id': channel.id,
                'category_id': section.id,
                'sequence': seq,
                'slide_category': 'article',
                'is_published': True,
                # Free preview for the orientation + first two sections;
                # creation path only — existing slides are never touched.
                'is_preview': section_data['name'] in PREVIEW_SECTION_NAMES,
                'completion_time': lesson_data['hours'],
                'tag_ids': [(6, 0, [tags[lesson_data['level']].id])],
                'description': lesson_data['summary'],
                'html_content': lesson_data['html'],
            })
            created_lessons += 1
    _logger.info(
        'prospire_elearning: curriculum sync on channel %r done: %s section(s) '
        'and %s lesson(s) created',
        channel.name, created_sections, created_lessons,
    )


def _setup_course(env):
    Channel = env['slide.channel'].sudo()
    Slide = env['slide.slide'].sudo()
    Tag = env['slide.tag'].sudo()

    tags = {
        level: _get_or_create_tag(Tag, level)
        for level in ('Beginner', 'Intermediate', 'Advanced')
    }

    channel = _resolve_target_channel(Channel, env)
    if not channel:
        _logger.warning('prospire_elearning: no target channel available, aborting')
        return

    _apply_channel_branding(env, channel)
    _archive_legacy_channel(env, Channel, Slide, channel)

    existing = _archive_sample_slides(Slide, channel)

    seq = max(existing.mapped('sequence') or [0])
    seq = _create_orientation(Slide, channel, seq)
    _create_curriculum(Slide, channel, tags, seq, existing)
