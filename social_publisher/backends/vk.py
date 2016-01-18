# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
from django.conf import settings
from social_publisher import vk
from social_publisher.backends import base


class VKBackend(base.BaseBackend):
    name = 'vk'
    auth_provider = 'vk-oauth'
    DEFAULT_PERMISSION_FOR_CHECK = 8192

    def get_api(self, social_user):
        return vk.API(access_token=social_user.extra_data.get('access_token'),
                      app_id=settings.VK_APP_ID, scope=['photos', 'wall'])

    def get_api_publisher(self, social_user):
        """
            owner_id - VK user or group
            from_group - 1 by group, 0 by user
            message - text
            attachments - comma separated links or VK resources ID's
            and other https://vk.com/dev.php?method=wall.post
        """

        def _post(**kwargs):
            api = self.get_api(social_user)
            response = api.wall.post(**kwargs)
            return response

        return _post

    def check(self, permission=None, social_user=None):
        api = self.get_api(social_user or self.social_user)
        permission = permission or self.DEFAULT_PERMISSION_FOR_CHECK

        try:
            perm_mask = int("{0:b}".format(api.getUserSettings()), 2)
            return perm_mask & int("{0:b}".format(permission), 2) == permission
        except Exception:
            return False


class VKImageToWallBackend(VKBackend):
    name = 'vk_image_to_wall'
    auth_provider = 'vk-standalone'

    def get_api_publisher(self, social_user):
        """
            files: {'file0':<file>}
            message: 'mess'
        """

        def _post(**kwargs):
            api = self.get_api(social_user)
            author = {
                'group_id': kwargs.get('group_id'),
                'user_id': kwargs.get('user_id'),
            }
            server_data = api.photos.getWallUploadServer(**author)
            attachments = []

            for _file in kwargs['files']:
                upload_data = requests.post(
                    server_data['upload_url'], files={"photo": _file}).json()
                upload_data.update(author)
                photos_data = api.photos.saveWallPhoto(**upload_data)
                attachments.append('photo{owner_id}_{id}'.format(**photos_data[0]))

            del kwargs['files']
            kwargs['attachments'] = ','.join(attachments)
            response = api.wall.post(**kwargs)

            server_data.update(response)
            return server_data

        return _post
