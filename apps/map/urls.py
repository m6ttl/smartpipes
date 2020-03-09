# encoding: utf-8
# from map.views import test
from map import views

__author__ = '易维科技'
__date__ = '2018/1/12 0012 03:28'

from django.urls import path, re_path
from django.conf.urls import url

app_name = "map"

urlpatterns = [

    # 百度地图
    # path('map/', map.as_view(), name="map"),
    url(r'$', views.test),
]