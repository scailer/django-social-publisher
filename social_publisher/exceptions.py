# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class NoAccess(Exception):
    pass


class ExternalAPIError(Exception):
    pass


class SocialUserDoesNotExist(Exception):
    pass
