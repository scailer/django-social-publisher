# -*- coding: utf-8 -*-

from social_publisher import twython
from django.conf import settings
from django.http import QueryDict
from social_publisher.backends import base


class TwitterBackend(base.BaseBackend):
    name = 'twitter'
    auth_provider = 'twitter'
    exceptions = (twython.TwythonAuthError,)

    def get_api(self, social_user):
        data = QueryDict(social_user.extra_data['access_token'])

        twitter = twython.Twython(
            settings.TWITTER_CONSUMER_KEY,
            settings.TWITTER_CONSUMER_SECRET,
            data['oauth_token'],
            data['oauth_token_secret']
        )

        return twitter

    def get_api_publisher(self, social_user):
        return self.get_api(social_user).update_status


class TwitterWithMediaBackend(TwitterBackend):
    name = 'twitter_with_media'
    auth_provider = 'twitter'

    def get_api_publisher(self, social_user):
        return self.get_api(social_user).update_status_with_media
