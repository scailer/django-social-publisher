# -*- coding: utf-8 -*-

from django.utils.encoding import smart_unicode


class DefaultHandler(object):
    def __init__(self, backend, context):
        self.backend = backend
        self.context = context

    def pre_handle(self, obj, comment):
        return {'text': comment or smart_unicode(obj)}

    def post_handle(self, result):
        return 'http://example.com/', result
