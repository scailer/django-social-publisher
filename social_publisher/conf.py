# -*- coding: utf-8 -*-

from django.conf import settings

SOCIAL_PUBLIC_DEBUG = getattr(settings, 'SOCIAL_PUBLIC_DEBUG', True)
SOCIAL_PUBLIC_BACKENDS = getattr(settings, 'SOCIAL_PUBLIC_BACKENDS', [])
SOCIAL_PUBLIC_HANDLERS = getattr(settings, 'SOCIAL_PUBLIC_HANDLERS', {})
SOCIAL_PUBLIC_LOGGER_NAME = getattr(settings, 'SOCIAL_PUBLIC_LOGGER_NAME', 'publisher')
