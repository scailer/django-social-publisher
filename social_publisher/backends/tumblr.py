# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from social_publisher import pytumblr
from django.conf import settings
from social_publisher.backends import base


class TumblrBaseBackend(base.BaseBackend):
    name = 'tumblr'
    auth_provider = 'tumblr'
#    exceptions = (twython.TwythonAuthError,)

    def get_api(self, social_user):
        return pytumblr.TumblrRestClient(
            settings.SOCIAL_AUTH_TUMBLR_KEY,
            settings.SOCIAL_AUTH_TUMBLR_SECRET,
            social_user.extra_data['access_token']['oauth_token'],
            social_user.extra_data['access_token']['oauth_token_secret']
        )

    def get_api_publisher(self, social_user):
        return self.get_api(social_user).create_text

    def check(self, permission=None, social_user=None):
        api = self.get_api(social_user or self.social_user)

        try:
            return bool(api.info().get('user'))
        except Exception:
            return False


class TumblrPhotoBackend(TumblrBaseBackend):
    name = 'tumblr_photo'

    def get_api_publisher(self, social_user):
        uid = social_user.uid

        def _func(**data):
            _uid = data.get('uid', uid)
            data['state'] = data.get('state', 'published')
            return self.get_api(social_user).create_photo(_uid, **data)

        return _func
