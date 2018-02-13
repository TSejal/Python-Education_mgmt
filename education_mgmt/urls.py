from django.conf.urls import patterns, include, url
from django.contrib import admin

print "in main url"
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
)