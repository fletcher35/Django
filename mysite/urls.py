from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from wall.views import *
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<pk>\d+)/$', detail),
)
