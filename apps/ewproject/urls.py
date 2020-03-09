# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/13 0013 01:57'

# encoding: utf-8
from ewproject.views import *
from django.urls import path, re_path


app_name = "ewprojectapp"
urlpatterns = [
    # 课程列表url
    path('ewprojectp/', ewprojectView.as_view(), name="ewprojectn"),
    path('hello/', helloView.as_view(), name="hello"),
    path('know/', know1View.as_view(), name="know"),
    path('sub/', htmlsubView.as_view(), name="sub"),
    path('cost/', listcostView.as_view(), name="cost"),
    path('report/', ReportListView.as_view(), name="report"),
]

