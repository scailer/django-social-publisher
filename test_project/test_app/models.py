# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from social_publisher import mixins


class User(AbstractUser, mixins.SocialPublicForUserMixin):
    pass
