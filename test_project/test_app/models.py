# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from social_publisher import mixins


class User(AbstractUser, mixins.PublisherForUserMixin):
    pass
