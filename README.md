django_social_publisher
=======================

Extension for django-social-auth [https://pypi.python.org/pypi/django-social-auth/] 
that add ability to create posts in social nets from registered user directly.

Module contains pluggable system of social-nets backends and handlers for adapt 
user content to social nets API format.

For writing you own haandlers, see examples in source code.


## START ##

```sh
$ pip install django_social_publisher
```

project/settings.py
```python
INSTALLED_APPS = (
    ...
    'social_auth',
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
    'social_auth.backends.twitter.TwitterBackend',      # twitter
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
    'social_auth.backends.facebook.FacebookBackend',    # facebook
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


## Extra settings ##

project/settings.py
```python
PUBLISHER_DEFAULT_HANDLER = 'social_publisher.handlers.default.DefaultHandler'
PUBLISHER_LOGGER_NAME = 'my_logger'
PUBLISHER_PUBLIC_DEBUG = True  # if False, errors fails silently and writes log
```
