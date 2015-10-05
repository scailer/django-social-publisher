# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
from social_publisher import conf

logger = logging.getLogger(conf.PUBLISHER_LOGGER_NAME)


def _safe_call(func):
    def _f(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:
            if conf.PUBLISHER_DEBUG:
                raise

            logger.error('FAIL %s: %s', func,
                         e.args and e.args[0] or '_no_info_')

    return _f


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
