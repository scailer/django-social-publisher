# -*- coding: utf-8 -*-

from social_publisher.handlers import default


class TumblrPhotoHandler(default.DefaultHandler):
    def pre_handle(self, obj, comment):
        return {
            'tags': [],
            'source': '',
        }

    def post_handle(self, result, data, obj, comment):
        return '', result
