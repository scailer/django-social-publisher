import os
from .secret import *

DEBUG = True
TEMPLATE_DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = []
AUTH_USER_MODEL = 'test_app.User'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'test_app',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# Social
AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',  # google-oauth
#    'social.backends.contrib.vk.VKOAuth2',  # vk-oauth
    'social.backends.twitter.TwitterOAuth',      # twitter
    'social.backends.facebook.Facebook2OAuth2',    # facebook
#    'social_publisher.auth.vk.VKStandaloneBackend',     # vk-standalone
)

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_DEFAULT_USERNAME = lambda: random.choice(['Darth_Vader', 'Obi-Wan_Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])
SOCIAL_AUTH_CREATE_USERS = True

GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True
GOOGLE_OAUTH2_AUTH_EXTRA_ARGUMENTS = {
    'access_type': 'offline',
}
GOOGLE_SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

VK_OAUTH2_EXTRA_SCOPE = ['wall', 'photos', 'offline']
VK_OAUTH_AUTH_EXTRA_ARGUMENTS = {
    'redirect_uri': 'blank.html',
    'response_type': 'token',
}

TWITTER_SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'en_US'}
FACEBOOK_SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
FACEBOOK_EXTENDED_PERMISSIONS = ['email', 'publish_actions']

PUBLISHER_BACKENDS = (
    'social_publisher.backends.twitter.TwitterBackend',
    'social_publisher.backends.twitter.TwitterWithMediaBackend',
    'social_publisher.backends.facebook.FacebookBackend',
    'social_publisher.backends.facebook.FacebookPostImageBackend',
#    'social_publisher.backends.vk.VKImageToWallBackend',
)
PUBLISHER_HANDLERS = {
    'twitter':              'social_publisher.handlers.twitter.TwitterHandler',
    'twitter_with_media':   'social_publisher.handlers.twitter.TwitterWithMediaHandler',
    'facebook':             'social_publisher.handlers.facebook.FacebookMessageHandler',
    'facebook_post_image':  'social_publisher.handlers.facebook.FacebookPhotoHandler',
#    'vk_image_to_wall':     'social_publisher.handlers.vk.VKImageToWallHandler'
}

PUBLISHER_DEFAULT_HANDLER = 'social_publisher.handlers.default.DefaultHandler'
