# -*- coding: utf-8 -*-

from . import conf

if any('facebook' in x for x in conf.SOCIAL_PUBLIC_BACKENDS):
    import facebook

if any('.vk.' in x for x in conf.SOCIAL_PUBLIC_BACKENDS):
    import vk
