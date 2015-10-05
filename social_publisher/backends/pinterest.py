# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
from social_publisher.backends import base


class PinterestBackend(base.BaseBackend):
    name = 'pinterest'
    auth_provider = 'pinterest'

    def get_api_publisher(self, social_user):
        data = {
            'access_token': social_user.extra_data.get('access_token'),
            'board_id': social_user.extra_data.get('board_id'),
        }

        def _post(description, image_url):
            data.update({'description': description, 'image_url': image_url})
            response = requests.put('https://api.pinterest.com/v3/pins/', data)
            return response.json()

        return _post
