# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from social_publisher import twython
from django.conf import settings
from social_publisher.backends import base


class TwitterBackend(base.BaseBackend):
    name = 'twitter'
    auth_provider = 'twitter'
    exceptions = (twython.TwythonAuthError,)

    def get_api(self, social_user):
        return twython.Twython(
            settings.SOCIAL_AUTH_TWITTER_KEY,
            settings.SOCIAL_AUTH_TWITTER_SECRET,
            social_user.extra_data['access_token']['oauth_token'],
            social_user.extra_data['access_token']['oauth_token_secret']
        )

    def get_api_publisher(self, social_user):
        return self.get_api(social_user).update_status

    def check(self, permission=None, social_user=None):
        api = self.get_api(social_user or self.social_user)

        try:
            return bool(api.verify_credentials())
        except Exception:
            return False


class TwitterWithMediaBackend(TwitterBackend):
    name = 'twitter_with_media'
    auth_provider = 'twitter'

    def get_api_publisher(self, social_user):
        api = self.get_api(social_user)

        def _func(media, status=''):
            media_data = api.upload_media(media=media)
            return api.update_status(
                status=status, media_ids=media_data['media_id'])

        return _func
