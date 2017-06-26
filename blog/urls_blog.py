from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'home/$', views.index, name='index'),
        url(r'articles/$', views.post_list, name='post_list'),
        url(r'projects/$', views.projects, name='projects'),
        url(r'resume/$', views.resume, name='resume'),
]
