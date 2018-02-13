from django.conf.urls import patterns, url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from api.views import *
from rest_framework.authtoken import views as tokenView


print "in api url"

urlpatterns = patterns('',
    url(r'^login/$', tokenView.obtain_auth_token),

    url(r'^register/$', user_register, name='user-register'),

    url(r'^student/add/$', add_student, name='add-student'),

    url(r'^university/add/$', add_university, name='add-university'),
    url(r'^university/list/$', university_list, name='university-list'),
    url(r'^university/list1/$', universitywithschools_list, name='university-school-list'),
    url(r'^university/delete/(?P<pk>[0-9]+)/$', university_delete, name='university-delete'),

    url(r'^school/add/$', add_school, name='add-school'),
    url(r'^school/list/$', school_list, name='school-list'),
    url(r'^school/details/(?P<pk>[0-9]+)/$', school_details, name='school-detail'),
    url(r'^school/update/(?P<pk>[0-9]+)/$', school_update, name='school-update'),
    url(r'^school/delete/(?P<pk>[0-9]+)/$', school_delete, name='school-delete'),
)





