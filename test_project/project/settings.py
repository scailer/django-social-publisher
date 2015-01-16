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
    'social_auth',
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
    'social_auth.backends.google.GoogleOAuth2Backend',  # google-oauth
    'social_auth.backends.contrib.vk.VKOAuth2Backend',  # vk-oauth
    'social_auth.backends.twitter.TwitterBackend',      # twitter
    'social_auth.backends.facebook.FacebookBackend',    # facebook
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