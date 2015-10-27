# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from social_publisher import conf

if any('facebook' in x for x in conf.PUBLISHER_BACKENDS):
    import facebook  #NOQA

if any('twitter' in x for x in conf.PUBLISHER_BACKENDS):
    import twython  #NOQA

if any('.vk.' in x for x in conf.PUBLISHER_BACKENDS):
    import vk  #NOQA

if any('.tumblr.' in x for x in conf.PUBLISHER_BACKENDS):
    import pytumblr  #NOQA
