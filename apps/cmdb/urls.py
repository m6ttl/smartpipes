# encoding: utf-8
from cmdb.views import EchartView

__author__ = '易维科技'
__date__ = '2018/1/12 0012 03:28'

from django.urls import path, re_path

app_name = "cmdb"

urlpatterns = [

    # 课程类型列表url
    path('Echart/', EchartView.as_view(), name="echart"),
]