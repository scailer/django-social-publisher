# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import odnoklassniki
from django.conf import settings
from social_publisher.backends import base


class OKBackend(base.BaseBackend):
    name = 'ok'
    auth_provider = 'odnoklassniki'

    def get_api(self, social_user):
        return odnoklassniki.Odnoklassniki(
            client_key=settings.ODNOKLASSNIKI_OAUTH2_CLIENT_KEY,
            client_secret=settings.ODNOKLASSNIKI_OAUTH2_CLIENT_SECRET,
            token=social_user.extra_data.get('access_token')
        )

    def get_api_publisher(self, social_user):
        """
            and other https://vk.com/dev.php?method=wall.post
        """

        def _post(**kwargs):
            api = self.get_api(social_user)
            from pudb import set_trace; set_trace()
            # api.group.getInfo('uids'='your_group_id', 'fields'='members_count')
            #response = api.wall.post(**kwargs)
            return response

        return _post
