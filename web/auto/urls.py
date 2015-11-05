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

]