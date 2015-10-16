from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^item/(?P<name>\w+)/$', views.item, name='item'),

]
