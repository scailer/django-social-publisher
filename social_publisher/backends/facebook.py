# -*- coding: utf-8 -*-

from social_publisher import facebook
from . import base


class FacebookBackend(base.BaseBackend):
    name = 'facebook'
    auth_provider = 'facebook'

    def get_api(self, social_user):
        return facebook.GraphAPI(social_user.extra_data.get('access_token'))

    def get_api_publisher(self, social_user):
        """
            message: str
            attachment: {name, link, caption, description, picture}
        """
        def _post(self, **kwargs):
            return self.get_api(social_user).post('me/feed', params=kwargs)

        return _post


class FacebookPostImageBackend(FacebookBackend):
    name = 'facebook_post_image'
    auth_provider = 'facebook'

    def get_api_publisher(self, social_user):
        """
            message: str
            attachment: {name, link, caption, description, picture}
        """
        def _post(**kwargs):
            return self.get_api(social_user).post('me/photos', params=kwargs)

        return _post
