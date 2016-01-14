url__author__ = 'bob.zhu'
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'api/read_log/(?P<feature_id>[0-9]+)/$', views.read_log, name='read_log'),
    url(r'api/read_console/(?P<feature_id>[0-9]+)/$', views.read_console, name='read_console'),
    url(r'api/read_screenshot/(?P<feature_id>[0-9]+)/$', views.read_screenshot, name='read_screenshot'),
    url(r'api/read_screenshot_index/(?P<feature_id>[0-9]+)/$', views.read_screenshot_index, name='read_screenshot_index'),
    url(r'api/read_build_history/(?P<feature_id>[0-9]+)/$', views.read_build_history, name='read_build_history'),
    url(r'api/read_screenshot_by_path', views.get_screenshot_by_path, name='read_by_path')
]