# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class ExternalAPIError(Exception):
    pass


class AccessDenied(ExternalAPIError):
    pass


class SocialUserDoesNotExist(Exception):
    pass
