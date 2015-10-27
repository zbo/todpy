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

    # ex: /auto/sample
    url(r'sample', views.sample, name='sample'),
    # ex: /auto/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /auto/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /auto/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]