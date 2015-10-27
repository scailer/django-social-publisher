# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
from social_publisher.backends import base


class PinterestBackend(base.BaseBackend):
    name = 'pinterest'
    auth_provider = 'pinterest'

    def get_board(self, access_token, board_name):
        response = requests.get(
            'https://api.pinterest.com/v1/me/boards/?access_token={}'.format(
                access_token))

        data = response.json().get('data')
        board = [b for b in data if b.get('name') == board_name]

        if board:
            return board[0].get('id')

        response = requests.post(
            'https://api.pinterest.com/v1/boards/',
            data={
                'access_token': access_token,
                'name': board_name,
                'description': board_name,
            })

        return response.json().get('data', {}).get('id')

    def get_api_publisher(self, social_user):
        access_token = social_user.extra_data.get('access_token')

        def _post(image_url, note, link, board_name='publisher'):
            data = {
                'access_token': access_token,
                'board': self.get_board(access_token, board_name),
                'image_url': image_url,
                'note': note,
                'link': link,
            }
            response = requests.post('https://api.pinterest.com/v1/pins/', data)
            return response.json()

        return _post
