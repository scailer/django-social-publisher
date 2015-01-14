# -*- coding: utf-8 -*-

from . import default


class VKImageToWallHandler(default.DefaultHandler):
    def pre_handle(self, obj, comment):
        obj.picture.file.seek(0)
        return {'files': {'file0': obj.picture.file}}

    def post_handle(self, result):
        url = 'http://vk.com/wall{user_id}_{post_id}'.format(**result)
        return url, result

    def exception_handle(self, e, backend):
        pass
