# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.module_loading import import_string as _load
from social_publisher.exceptions import ExternalAPIError
from social_publisher import conf


class BaseBackend(object):
    name = 'base'
    default_handler = _load(conf.PUBLISHER_DEFAULT_HANDLER)
    exceptions = ()

    def __init__(self, social_user, context):
        self.context = context
        self.social_user = social_user
        self.publisher = self.get_api_publisher(social_user)

    def get_api_publisher(self, social_user):
        raise NotImplementedError('Implement in subclass')

    def check(self, permission=None, social_user=None):
        raise NotImplementedError('Implement in subclass')

    def get_handler(self):
        handlers = self.context['core'].handlers
        return handlers.get(self.name, self.default_handler)

    def publish(self, obj, comment):
        Handler = self.get_handler()
        handler = Handler(backend=self, context=self.context)
        data = handler.pre_handle(obj, comment)

        try:
            if isinstance(data, str):
                response = self.publisher(data)

            elif isinstance(data, dict):
                response = self.publisher(**data)

            elif isinstance(data, list):
                response = self.publisher(*data)

            elif isinstance(data, tuple):
                args, kwargs = [], {}

                for x in data:
                    if isinstance(x, dict):
                        kwargs = x
                    else:
                        args.append(x)

                response = self.publisher(*args, **kwargs)

        except self.exceptions as e:
            handler.exception_handle(e, data=data, obj=obj, comment=comment)
            raise ExternalAPIError()

        return handler.post_handle(
            response, data=data, obj=obj, comment=comment)
