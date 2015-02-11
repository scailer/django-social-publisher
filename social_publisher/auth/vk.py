# -*- coding: utf-8 -*-

from django.conf import settings
from social_auth.backends.contrib.vk import VKOAuth2Backend, VKOAuth2


class VKStandaloneBackend(VKOAuth2Backend):
    name = 'vk-standalone'


class VKStandaloneAuth(VKOAuth2):
    name = 'vk-standalone'
    AUTH_BACKEND = VKStandaloneBackend
    SETTINGS_KEY_NAME = 'VK_STANDALONE_APP_ID'
    SETTINGS_SECRET_NAME = 'VK_STANDALONE_API_SECRET'

    def get_scope(self):
        scope = super(VKStandaloneAuth, self).get_scope()
        scope = list(scope) if scope else []
        extra = getattr(settings, 'VK_STANDALONE_EXTRA_SCOPE', [])
        scope.extend(extra)
        return scope

    def auth_complete(self, *args, **kwargs):
        request = kwargs.get('request')
        params = request.GET.dict()
        return self.do_auth(params['access_token'], response=params,
                            *args, **kwargs)


BACKENDS = {
    'vk-standalone': VKStandaloneAuth,
}
