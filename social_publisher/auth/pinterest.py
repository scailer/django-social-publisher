# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
from django.conf import settings

from social.p3 import urlencode
from social.utils import handle_http_errors
from social.backends.oauth import BaseOAuth1


class PinterestOauth(BaseOAuth1):
    name = 'pinterest'
    RESPONSE_TYPE = 'token'
    AUTHORIZE_URL = AUTHORIZATION_URL = 'https://www.pinterest.com/oauth/'
    ACCESS_TOKEN_URL = 'https://api.pinterest.com/oauth/access_token'
    REQUEST_TOKEN_URL = AUTHORIZE_URL

    def oauth_authorization_request(self, token):
        params = self.setting('AUTH_EXTRA_ARGUMENTS', {}).copy()
        params.update({
            'consumer_id': settings.SOCIAL_AUTH_PINTEREST_KEY,
            'response_type': self.RESPONSE_TYPE,
        })
        return '{0}?{1}'.format(self.authorization_url(), urlencode(params))

    @handle_http_errors
    def auth_complete(self, *args, **kwargs):
        self.process_error(self.data)
        self.validate_state()
        access_token = self.data.get('access_token')
        return self.do_auth(access_token, *args, **kwargs)

    @handle_http_errors
    def do_auth(self, access_token, *args, **kwargs):
        data = self.user_data(access_token)
        if data is not None and 'access_token' not in data:
            data['access_token'] = access_token
        kwargs.update({'response': data, 'backend': self})
        return self.strategy.authenticate(*args, **kwargs)

    def user_data(self, access_token, *args, **kwargs):
        for x in range(5):
            response = requests.put(
                'https://api.pinterest.com/v3/boards/?join=owner',
                {'access_token': access_token, 'name': 'comixon'})

            if response.status_code == 200:
                return response.json().get('data', {})

        return {}

    def get_user_id(self, details, response):
        return response.get('owner', {}).get('id')

    def get_user_details(self, response):
        # TODO: get data normaly, not from board
        user_data = response.get('owner', {})
        return {
            'username': user_data.get('username'),
            'email': None,
            'fullname': user_data.get('full_name'),
            'first_name': user_data.get('first_name'),
            'last_name': user_data.get('last_name'),
            'userpic': user_data.get('image_large_url'),
        }

    def extra_data(self, user, uid, response, details=None, *args, **kwargs):
        data = super(PinterestOauth, self).extra_data(
            user, uid, response, details, *args, **kwargs)
        data['board_id'] = response['id']
        return data
