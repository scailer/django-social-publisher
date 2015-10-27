# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings

PUBLISHER_DEBUG = getattr(settings, 'PUBLISHER_DEBUG', True)
PUBLISHER_BACKENDS = getattr(settings, 'PUBLISHER_BACKENDS', [])
PUBLISHER_HANDLERS = getattr(settings, 'PUBLISHER_HANDLERS', {})
PUBLISHER_LOGGER_NAME = getattr(settings, 'PUBLISHER_LOGGER_NAME', 'publisher')
PUBLISHER_DEFAULT_HANDLER = getattr(
    settings, 'PUBLISHER_DEFAULT_HANDLER',
    'social_publisher.handlers.default.DefaultHandler')
