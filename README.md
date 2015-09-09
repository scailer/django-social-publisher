django_social_publisher
=======================

Extension for python-social-auth [https://pypi.python.org/pypi/python-social-auth/] 
that add ability to create posts in social nets from registered user directly.

Module contains pluggable system of social-nets backends and handlers for adapt 
user content to social nets API format.

For writing you own haandlers, see examples in source code.

Normally works for *twitter*, *facebook* and *tumblr*.

Works with hacks for *VK*, *pinterest*.


### Start ###

```sh
$ pip install django_social_publisher
```

project/settings.py
```python
INSTALLED_APPS = (
    ...
    'social.apps.django_app.default',
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
AUTH_USER_MODEL = 'test_app.User'
```

account/models.py
```python
from social_publisher import mixins
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, mixins.PublisherForUserMixin):
    pass
```

Base usage:

```python
user.publish.<provider_name>(obj, comment, **kwargs)
user.publish_to(provider_name, obj, comment, **kwargs)
```

### Twitter ###

```sh
$ pip install twython
```

project/settings.py
```python
AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterBackend',      # twitter
    ...
)

PUBLISHER_BACKENDS = (
    'social_publisher.backends.twitter.TwitterBackend',  # basic text message / provider name - twitter
    'social_publisher.backends.twitter.TwitterWithMediaBackend',  # you custom message / provider name - twitter_with_media
    ...
)

PUBLISHER_HANDLERS = {
    # '<provider_name>': 'you.handler.MyHandler'
    'twitter': 'social_publisher.handlers.twitter.TwitterHandler',
    'twitter_with_media': 'social_publisher.handlers.twitter.TwitterWithMediaHandler',
    ...
}

TWITTER_CONSUMER_KEY = '016UBm0dJQVy1dlJNv0G7n3M'
TWITTER_CONSUMER_SECRET = 'ii7KEsHUHxGF5k1aFHZjNExEhPmE9B3WcIhAWDrzX29JSbqKY'
TWITTER_SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
```

Usage:

```python
from test_app.models import User
user1 = User.objects.get(username='user1')
user1.publish.twitter('Test message')
user1.publish.twitter_with_media(obj)  # obj - you data for you custom handler
```

### Facebook ###

```sh
$ pip install requests-facebook sorl-thumbnail
```

project/settings.py
```python
AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookBackend',    # facebook
    ...
)

PUBLISHER_BACKENDS = (
    'social_publisher.backends.facebook.FacebookBackend',  # basic text message / provider name - facebook
    'social_publisher.backends.facebook.FacebookPostImageBackend',  # you custom message / provider name - facebook_post_image
    ...
)

PUBLISHER_HANDLERS = {
    # '<provider_name>': 'you.handler.MyHandler'
    'facebook':     'social_publisher.handlers.facebook.FacebookMessageHandler',
    'facebook_post_image': 'social_publisher.handlers.facebook.FacebookPhotoHandler',
    ...
}

FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}
FACEBOOK_SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'publish_actions']
FACEBOOK_APP_ID = '000016257465000'
FACEBOOK_API_SECRET = 'a0000000000003ef94c343382537c60'
```

Usage:

```python
from test_app.models import User
user1 = User.objects.get(username='user1')
user1.publish.facebook('Test message')
user1.publish.facebook_post_image(obj)  # obj - you data for you custom handler
```


### Tumblr ###

```sh
$ pip install PyTumblr
```

project/settings.py
```python
AUTHENTICATION_BACKENDS = (
    'social.backends.tumblr.TumblrOAuth',
    ...
)

PUBLISHER_BACKENDS = (
    'social_publisher.backends.tumblr.TumblrPhotoBackend',
    ...
)

PUBLISHER_HANDLERS = {
    'tumblr_photo': 'social_publisher.handlers.tumblr.TumblrPhotoHandler',  # use as example
    ...
}
```

SOCIAL_AUTH_TUMBLR_KEY = 'XXXXXXXXXXXXXXXXXXXXXFSZboiEYvCm3I8HOToVjRNrIgMo6J'
SOCIAL_AUTH_TUMBLR_SECRET = 'jV173bMZFjvNiybCvdEx6cjITXXXXXXXXXXXXXXXXXXXXXXXXX'


### ВКонтакте ###

Works only with hacks, no official way.

Warning! You need catch response from VK on client side, fix it - 
replace "#" by "?" and send secret keys to the server.

```sh
$ pip install vk
```

project/settings.py
```python
AUTHENTICATION_BACKENDS = (
    'social_publisher.auth.vk.VKStandaloneBackend',
    ...
)

PUBLISHER_BACKENDS = (
    'social_publisher.backends.vk.VKImageToWallBackend',
    ...
)

PUBLISHER_HANDLERS = {
    'vk_image_to_wall': 'social_publisher.handlers.vk.VKImageToWallHandler',  # use as example
    ...
}
```


### Pinterest ###

Works only with hacks, no official way.

Warning! You need catch response from VK on client side, fix it - 
replace "#" by "?" and send secret keys to the server.

```sh
$ pip install requests 
```

project/settings.py
```python
AUTHENTICATION_BACKENDS = (
    'social_publisher.auth.pinterest.PinterestOauth',
    ...
)

PUBLISHER_BACKENDS = (
    'social_publisher.backends.pinterest.PinterestBackend',
    ...
)

PUBLISHER_HANDLERS = {
    'pinterest': 'social_publisher.handlers.pinterest.PinterestHandler',  # use as example
    ...
}


SOCIAL_AUTH_PINTEREST_KEY = '1111111'
SOCIAL_AUTH_PINTEREST_SECRET = 'XXXXc1d1'
SOCIAL_AUTH_PINTEREST_AUTH_EXTRA_ARGUMENTS = {
    'no_auto_redirect_or_interstitial': '1'
}
```


### G+ ###

I don't know ways post to G+


### Extra settings ###

project/settings.py
```python
PUBLISHER_DEFAULT_HANDLER = 'social_publisher.handlers.default.DefaultHandler'
PUBLISHER_LOGGER_NAME = 'my_logger'
PUBLISHER_DEBUG = True  # if False, errors fails silently and writes log
```

---
The author brings apologies for my english.
