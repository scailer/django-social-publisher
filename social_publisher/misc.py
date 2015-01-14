# -*- coding: utf-8 -*-

import logging
from . import conf

logger = logging.getLogger(conf.SOCIAL_PUBLIC_LOGGER_NAME)


def _safe_call(func):
    def _f(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except Exception as e:
            if conf.SOCIAL_PUBLIC_DEBUG:
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
