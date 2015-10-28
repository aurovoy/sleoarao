from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items/$', views.itemlist, name='itemlist'),
#    url(r'^items/(?P<object_id>\d+)/$', views.itemdetail, name='item_detail'),
#    url(r'^photos/(?P<object_id>\d+)/$', views.photodetail, name='photo_detail'),


]
