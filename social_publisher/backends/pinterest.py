# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
from social_publisher.backends import base


class PinterestAPI(object):
    URL = 'https://api.pinterest.com/v1/'

    def __init__(self, access_token):
        self.token = access_token

    def __getattr__(self, name):
        if name in ('get', 'delete'):
            def _api(url, **kwargs):
                url = '{}{}/?access_token={}'.format(self.URL, url, self.token)
                getattr(requests, name)(url, **kwargs)

        elif name in ('put', 'post', 'patch'):
            def _api(url, data=None, **kwargs):
                url = '{}{}/'.format(self.URL, url)
                data['access_token'] = self.token
                getattr(requests, name)(url, data, **kwargs)

        return _api


class PinterestBackend(base.BaseBackend):
    name = 'pinterest'
    auth_provider = 'pinterest'

    def get_api(self, social_user):
        access_token = social_user.extra_data.get('access_token')
        return PinterestAPI(access_token)

    def get_board(self, api, board_name):
        response = api.get('me/boards')
        data = response.json().get('data')
        board = [b for b in data if b.get('name') == board_name]

        if board:
            return board[0].get('id')

        response = api.post('boards',
            data={
                'access_token': access_token,
                'name': board_name,
                'description': board_name,
            })

        return response.json().get('data', {}).get('id')

    def get_api_publisher(self, social_user):
        api = self.get_api(social_user)

        def _post(image_url, note, link, board_name='publisher'):
            data = {
                'board': self.get_board(api, board_name),
                'image_url': image_url,
                'note': note,
                'link': link,
            }
            response = api.post('pins', data)
            return response.json()

        return _post

    def check(self, permission=None, social_user=None):
        api = self.get_api(social_user or self.social_user)

        try:
            return api.get('me').ok
        except Exception:
            return False
