url__author__ = 'bob.zhu'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /auto/
    # url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.features, name='features'),
    # ex: /auto/create
    url(r'create', views.create, name='create'),
    url(r'accounts/login/', views.login, name="login"),
    url(r'accounts/auth/', views.do_login, name="do_login"),
    url(r'accounts/logout/', views.logout, name="login"),

    # ex: /auto/search_steps
    url(r'search_steps', views.search_steps, name='search_steps'),
    url(r'save_feature', views.save_feature, name='save_feature'),
    url(r'api/feature/(?P<feature_id>[0-9]+)/$', views.get_feature, name='get_feature'),
    url(r'update_feature/(?P<feature_id>[0-9]+)/$', views.update_feature, name='update_feature'),
    url(r'feature/list', views.list_features, name='list_features'),
    url(r'features', views.features, name='features'),
    url(r'feature/(?P<feature_id>[0-9]+)/$', views.viewDetail, name='feature'),
    url(r'feature/exe/(?P<feature_id>[0-9]+)/$', views.exe_feature, name='exe_feature'),
    url(r'feature/exe-status/(?P<feature_id>[0-9]+)/$', views.exe_feature_status, name='exe_feature_status'),
    url(r'testplan/(?P<testplan_id>[0-9]+)/$', views.testplan, name='testplan'),
    url(r'testplans', views.list_testplans, name='list_testplans')

]