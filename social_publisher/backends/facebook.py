# -*- coding: utf-8 -*-

from social_publisher import facebook
from social_publisher.backends import base


class FacebookBackend(base.BaseBackend):
    name = 'facebook'
    auth_provider = 'facebook'

    def get_api(self, social_user):
        return facebook.GraphAPI(social_user.extra_data.get('access_token'))

    def get_api_publisher(self, social_user):
        """
            message: <str>
            image: <file> as object_attachment
            owner_id: <str>
        """
        def _post(owner_id=None, **kwargs):
            owner_id = owner_id or 'me'
            image = kwargs.get('image')

            if image:
                res = self.get_api(social_user).post(
                    '{}/photos'.format(owner_id), image=image)
                kwargs['object_attachment'] = res['id']

            return self.get_api(social_user).post(
                '{}/feed'.format(owner_id),
                params=kwargs
            )

        return _post


class FacebookPostImageBackend(FacebookBackend):
    name = 'facebook_post_image'
    auth_provider = 'facebook'

    def get_api_publisher(self, social_user):
        """
            message: <str>
            image: <file>
            owner_id: <str>
        """
        def _post(owner_id=None, **kwargs):
            owner_id = owner_id or 'me'
            return self.get_api(social_user).post(
                '{}/photos'.format(owner_id),
                params=kwargs
            )

        return _post
