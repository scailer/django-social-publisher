# -*- coding: utf-8 -*-

from social_auth.backends.contrib.vk import VKOAuth2Backend, VKOAuth2


class VKStandaloneBackend(VKOAuth2Backend):
    name = 'vk-standalone'


class VKStandaloneAuth(VKOAuth2):
    name = 'vk-standalone'

    def auth_complete(self, *args, **kwargs):
        request = kwargs.get('request')
        params = request.GET.dict()
        return self.do_auth(params['access_token'], response=params,
                            *args, **kwargs)


BACKENDS = {
    'vk-standalone': VKStandaloneAuth,
}
