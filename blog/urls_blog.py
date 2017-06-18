from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
        #  url(r'^articles/', views.post_list, name='post_list'),
        #  url(r'^projects/', views.about, name='projects'),
        #  url(r'resume/', views.resume, name='resume'),
        #  url(r'contact/', views.contact, name='contact'),
]
