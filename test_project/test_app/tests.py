# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.test import TestCase


class LoadTest(TestCase):
    def test_load(self):
        from social_publisher import core, mixins
        from social_publisher.handlers import (facebook, tumblr, twitter, vk)
        from social_publisher.backends import (facebook, ok, pinterest,
                                               tumblr, twitter, vk)
