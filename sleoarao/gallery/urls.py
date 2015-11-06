from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^items/$', views.itemlist, name='itemlist'),
    url(r'^items/(?P<item_id>\d+)/$', views.itemdetail, name='item_detail'),
    url(r'^items/(?P<item_id>\d+)/(?P<photo_id>\d+)/$', views.photodetail, name='photo_detail'),
    url(r'^schedule/$', views.schedule, name='schedule'),


]
