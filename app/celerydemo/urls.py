from django.conf.urls import patterns, include, url
from django.contrib import admin
from celerydemo.views import homepage, sample_tasks_view

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', homepage),
    url(r'^sample_tasks', sample_tasks_view),
    url(r'^admin/', include(admin.site.urls)),
)
