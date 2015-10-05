# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import six
import traceback

from django.core.mail import mail_admins
from social_publisher.misc import logger


class DefaultHandler(object):
    def __init__(self, backend, context):
        self.backend = backend
        self.context = context

    def pre_handle(self, obj, comment):
        return {'text': comment or six.text_type(obj)}

    def post_handle(self, result, data, obj, comment):
        return 'http://example.com/', result

    def exception_handle(self, e, data, obj, comment):
        logger.error(str(e))
        subj = 'PUBLISHING ERROR {}: {}#{} [{}] by {}'.format(
            str(e), obj, obj.pk, self.backend.name, self.context.get('user'))
        message = 'Traceback:\n{}\n\n Data:\n{}\n Comment:\n{}'.format(
            traceback.format_exc(), data, comment)
        mail_admins(subj, message, fail_silently=True)
