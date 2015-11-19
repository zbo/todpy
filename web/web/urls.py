from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
import settings


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auto/', include('auto.urls')),
    url(r'^workspace/', include('workspace.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
