# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from social.backends.vk import VKOAuth2


class VKStandalone(VKOAuth2):
    name = 'vk-standalone'

    def auth_complete(self, *args, **kwargs):
        data = self.strategy.request_data()
        return self.do_auth(
            data['access_token'], response=data, *args, **kwargs)
