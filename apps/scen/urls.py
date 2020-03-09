# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/13 0013 01:57'

# encoding: utf-8
from scen.views import *
from django.urls import path, re_path


app_name = "scenapp"
urlpatterns = [
    path('index/', scenView.as_view(), name="scen"),
    # path('$', scenView.as_view(), name="scen"),
]

