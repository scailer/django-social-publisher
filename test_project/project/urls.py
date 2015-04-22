from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'test_app.views.user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social_auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
) + staticfiles_urlpatterns()
