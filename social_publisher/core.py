# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.module_loading import import_string as _load
from social.apps.django_app.default.models import UserSocialAuth
from social_publisher.exceptions import SocialUserDoesNotExist
from social_publisher import conf, misc


class PublisherCore(misc.Singleton):
    def __init__(self):
        self.load_backends()
        self.load_handlers()

    def load_backends(self):
        bckds = [_load(mod) for mod in conf.PUBLISHER_BACKENDS]
        self.backends = {backend.name: backend for backend in bckds}
        self.auth_provider_map = {backend.name: backend.auth_provider for backend in bckds}

    def load_handlers(self):
        hndls = conf.PUBLISHER_HANDLERS.items()
        self.handlers = {key: _load(mod) for key, mod in hndls}

    def find_backend(self, provider):
        try:
            return self.backends[provider]
        except KeyError:
            raise KeyError('provider must choose value from: {}'.format(
                ', '.join(self.backends.keys())))

    def get_backend(self, social_user, provider, context):
        Backend = self.find_backend(provider)
        context.update({
            'core': self,
            'provider': provider,
            'user': social_user.user,
        })
        return Backend(social_user, context=context)

    def find_social_user(self, user, provider):
        provider = self.auth_provider_map[provider]
        return user.social_auth.filter(provider=provider).first()

    def _get_social_user(self, user, provider):
        if isinstance(user, UserSocialAuth):
            social_user = user
        else:
            social_user = self.find_social_user(user, provider)

        if not social_user:
            raise SocialUserDoesNotExist()

        return social_user

    def get_api(self, user, provider, **kwargs):
        social_user = self._get_social_user(user, provider)
        backend = self.get_backend(social_user, provider, context=kwargs)
        return backend.get_api(social_user)

    def publish(self, user, provider, obj, comment, **kwargs):
        '''
            user - django User or UserSocialAuth instance
            provider - name of publisher provider
            obj - sharing object
            comment - string
        '''
        social_user = self._get_social_user(user, provider)
        backend = self.get_backend(social_user, provider, context=kwargs)
        return backend.publish(obj, comment)

    def check(self, user, provider, permission, **kwargs):
        '''
            user - django User or UserSocialAuth instance
            provider - name of publisher provider
            permission - if backend maintains check permissions
                            vk - binary mask in int format
                            facebook - scope string
        '''
        try:
            social_user = self._get_social_user(user, provider)
            if not social_user:
                return False

        except SocialUserDoesNotExist:
            return False

        backend = self.get_backend(social_user, provider, context=kwargs)
        return backend.check(permission)
