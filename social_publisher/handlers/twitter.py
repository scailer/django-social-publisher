# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from social_publisher.handlers import default


class TwitterHandler(default.DefaultHandler):
    def pre_handle(self, obj, comment):
        title = comment or obj.title
        postfix = '...' if (len(title) > 120) else ''
        return {
            'status': title[:110] + postfix,
        }

    def post_handle(self, result, data, obj, comment):
        return 'https://twitter.com/{}'.format(result['user']['screen_name']), result


# Example

class TwitterWithMediaHandler(TwitterHandler):
    def pre_handle(self, obj, comment):
        title = comment or obj.title
        postfix = '...' if (len(title) > 120) else ''
        return {
            'media': obj.picture.file,
            'status': title[:110] + postfix,
        }

    def post_handle(self, result, data, obj, comment):
        return result['entities']['media'][0]['expanded_url'], result
