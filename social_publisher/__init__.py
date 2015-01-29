# -*- coding: utf-8 -*-

from social_publisher import conf

if any('facebook' in x for x in conf.PUBLISHER_BACKENDS):
    import facebook

if any('twitter' in x for x in conf.PUBLISHER_BACKENDS):
    import twython

if any('.vk.' in x for x in conf.PUBLISHER_BACKENDS):
    import vk
