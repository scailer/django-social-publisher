# -*- coding: utf-8 -*-

from django.utils.encoding import smart_unicode
from social_publisher.misc import logger


class DefaultHandler(object):
    def __init__(self, backend, context):
        self.backend = backend
        self.context = context

    def pre_handle(self, obj, comment):
        return {'text': comment or smart_unicode(obj)}

    def post_handle(self, result, data, obj, comment):
        return 'http://example.com/', result

    def exception_handle(self, e, data, obj, comment):
        logger.error(str(e))
