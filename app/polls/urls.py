from django.conf.urls import patterns, include, url

from polls.views import create_poll_view

urlpatterns = patterns('',
    url(r'^harro/', create_poll_view),
)
