# -*- coding: utf-8 -*-

import requests
from django.conf import settings
from social_publisher import vk
from . import base


class VKImageToWallBackend(base.BaseBackend):
    name = 'vk_image_to_wall'
    auth_provider = 'vk-oauth'

    def get_api(self, social_user):
        return vk.API(access_token=social_user.extra_data.get('access_token'),
                      app_id=settings.VK_APP_ID, scope=['photos', 'wall'])

    def get_api_publisher(self, social_user):
        """
            files: {'file0':<file>}
            message: 'mess'
        """

        def _post(**kwargs):
            api = self.get_api(social_user)
            server_data = api.photos.getWallUploadServer()
            upload_data = requests.post(server_data['upload_url'],
                                        files=kwargs['files']).json()

            photos_data = api.photos.saveWallPhoto(**upload_data)
            kwargs['attachments'] = 'photo{owner_id}_{id}'.format(**photos_data[0])
            response = api.wall.post(**kwargs)

            server_data.update(response)
            return server_data

        return _post
