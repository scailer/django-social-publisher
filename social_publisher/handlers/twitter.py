# -*- coding: utf-8 -*-

from . import default


class TwitterHandler(default.DefaultHandler):
    def pre_handle(self, obj, comment):
        title = comment or obj.title
        postfix = '...' if (len(title) > 120) else ''
        return {
            'status': title[:110] + postfix,
        }

    def post_handle(self, result):
        return 'https://twitter.com/{}'.format(result['user']['screen_name']), result

    def exception_handle(self, e, backend):
        pass


# Example

class TwitterWithMediaHandler(TwitterHandler):
    def pre_handle(self, obj, comment):
        title = comment or obj.title
        postfix = '...' if (len(title) > 120) else ''
        return {
            'media': obj.picture.file,
            'status': title[:110] + postfix,
        }

    def post_handle(self, result):
        return result['entities']['media'][0]['expanded_url'], result
