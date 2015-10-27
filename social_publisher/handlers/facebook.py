# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import six

from social_publisher.handlers import default
from sorl.thumbnail import get_thumbnail


class FacebookMessageHandler(default.DefaultHandler):
    def pre_handle(self, obj, comment):
        return {'message': comment or six.text_type(obj)}

    def post_handle(self, result, data, obj, comment):
        return 'http://facebook.com/{}'.format(result['id']), result


# Example

class FacebookLinkHandler(FacebookMessageHandler):
    def pre_handle(self, obj, comment):
        return {
            'link': obj.picture.url,
            'picture': get_thumbnail(
                obj.picture, '128x128', crop='center').url,
            'name': comment or obj.title,
            'caption': obj.title,
            'description': '{} / {} via #servicename {}'.format(
                comment or obj.title, obj.user.get_full_name(),
                obj.time_created.strftime('%d %b %Y'))
        }


class FacebookPhotoHandler(FacebookMessageHandler):
    def pre_handle(self, obj, comment):
        return {
            'image': obj.picture,
            'message': comment or obj.title,
        }
