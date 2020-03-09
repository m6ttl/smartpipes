# encoding: utf-8
from django.conf.urls import url

__author__ = '易维科技'
__date__ = '2018/1/12 0012 03:28'

from django.urls import path, re_path
from . import views

# from django.conf.urls import url, include
# from dashing.utils import router

app_name = "ew_show_jl"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index),
    path('swwl/', views.swwl),
    path('dma/', views.dma),
    path('baoguanfenxi/', views.baoguanfenxi, name = 'baoguanfenxi'),
    path('gw/', views.gw),
    path('sp/', views.sp),
    path('css/', views.sp),
    path('zhgj/', views.zhgj, name = 'zhgj'),


]


