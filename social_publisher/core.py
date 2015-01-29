# -*- coding: utf-8 -*-

from django.utils.module_loading import import_by_path as _load
from .exceptions import SocialUserDoesNotExist
from . import conf, misc


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

    def get_backend(self, user, provider, context):
        social_user = self.find_social_user(user, provider)

        if not social_user:
            raise SocialUserDoesNotExist()

        Backend = self.find_backend(provider)
        context.update({'core': self, 'user': user, 'provider': provider})
        return Backend(social_user, context=context)

    def find_social_user(self, user, provider):
        provider = self.auth_provider_map[provider]
        return user.social_auth.filter(provider=provider).first()

    def publish(self, user, provider, obj, comment, **kwargs):
        return self.get_backend(user, provider, context=kwargs).publish(obj, comment)
