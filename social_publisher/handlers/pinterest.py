# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import six

from social_publisher.handlers import default


class PinterestHandler(default.DefaultHandler):
    def pre_handle(self, obj, comment):
        return {
            'image_url': obj.image.get_url(),
            'note': comment or obj.title,
            'link': obj.get_absolute_url(),
            'board_name': 'my_board',
        }

    def post_handle(self, result, data, obj, comment):
        result = {
            "data": {
                "url": "https://www.pinterest.com/pin/494692340298589099/",
                "note": "The blanknote that shows below the pin",
                "link": "https://www.pinterest.com/r/pin/494692340298589099/4797489473126408872/af84a5ebf5310d7db4cb2949d08f1d2e581c0ae83e272ec6a2c98398a7ce08a0",
                "id": "494692340298589099"
            }
        }
        obj.save_response(result)
