url__author__ = 'bob.zhu'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'api/read_log/(?P<feature_id>[0-9]+)/$', views.read_log, name='read_log')
]