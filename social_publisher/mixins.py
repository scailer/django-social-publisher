# -*- coding: utf-8 -*-

from . import core
from . import misc

_core = core.PublisherCore()


class Catcher(object):
    SocialUserDoesNotExist = core.SocialUserDoesNotExist

    def __init__(self, user, comment):
        self.user = user
        self.comment = comment

    def __getattr__(self, name):
        def _publish(*args, **kw):
            obj = kw.get('obj', args[0])
            _core.publish(self.user, name, obj, comment=self.comment, **kw)

        return misc._safe_call(_publish)


class PublisherForUserMixin(object):
    @property
    def publish(self, comment=None):
        return Catcher(user=self, comment=comment)

    def publish_to(self, provider, obj, **kw):
        return _core.publish(self, provider, obj, **kw)
