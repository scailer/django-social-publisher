# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from social_publisher import facebook
from social_publisher.backends import base


class FacebookBackend(base.BaseBackend):
    name = 'facebook'
    auth_provider = 'facebook'
    exceptions = (facebook.FacebookClientError, )
    DEFAULT_PERMISSION_FOR_CHECK = 'publish_actions'

    def get_api(self, social_user, owner_id=None):
        api = facebook.GraphAPI(social_user.extra_data.get('access_token'))

        if owner_id:
            try:
                user_accounts = api.get('me/accounts')
                access_token = [x["access_token"] for x in
                                user_accounts["data"] if x["id"] == owner_id]
                api = facebook.GraphAPI(access_token[0])

            except (KeyError, IndexError) as e:
                print('Get owner token failed: {}'.format(e))

        return api

    def get_api_publisher(self, social_user):
        """
            message: <str>
            image: <file> as object_attachment
            owner_id: <str>
        """

        def _post(owner_id=None, **kwargs):
            api = self.get_api(social_user, owner_id)
            return api.post('{}/feed'.format(owner_id or 'me'), params=kwargs)

        return _post

    def check(self, permission=None, social_user=None):
        api = self.get_api(social_user or self.social_user)
        permission = permission or self.DEFAULT_PERMISSION_FOR_CHECK

        try:
            data = api.get('me/permissions').get('data', [])
            perms = [d['permission'] for d in data if d['status'] == 'granted']
            return permission in perms
        except Exception:
            return False


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
            api = self.get_api(social_user, owner_id)
            return api.post('{}/photos'.format(owner_id or 'me'), params=kwargs)

        return _post
