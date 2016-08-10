#coding=utf-8

from django.conf.urls import patterns, include, url
from djangouser.auth_views import auth_login, auth_logout
from djangouser.user_views import UserList

urlpatterns = patterns('',
    url(r'^login/$', auth_login),
    url(r'^logout/$', auth_logout),
    url(r'^user/$', UserList.as_view()),
)
