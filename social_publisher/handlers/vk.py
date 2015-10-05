# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from social_publisher.handlers import default


class VKImageToWallHandler(default.DefaultHandler):
    def pre_handle(self, obj, comment):
        obj.picture.file.seek(0)
        return {'files': {'file0': obj.picture.file}}

    def post_handle(self, result, data, obj, comment):
        url = 'http://vk.com/wall{user_id}_{post_id}'.format(**result)
        return url, result
