__author__ = 'bob.zhu'
from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /auto/
    url(r'^$', views.index, name='index'),
    # ex: /auto/create
    url(r'create', views.create, name='create'),

    # ex: /auto/search_steps
    url(r'search_steps', views.search_steps, name='search_steps'),
    url(r'save_feature', views.save_feature, name='save_feature'),
    url(r'get_feature/(?P<feature_id>[0-9]+)/$', views.get_feature, name='get_feature'),
    url(r'update_feature/(?P<feature_id>[0-9]+)/$', views.update_feature, name='update_feature'),
    url(r'feature/list', views.list_features, name='list_features'),
    url(r'feature', views.features, name='features')


]