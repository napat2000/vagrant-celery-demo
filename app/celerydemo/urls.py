from django.conf.urls import patterns, include, url
from django.contrib import admin

from celerydemo.views import homepage
from polls.views import create_poll_view
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include("polls.urls")),
)
