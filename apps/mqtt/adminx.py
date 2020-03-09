# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import submsg


import xadmin

# ewPresales的admin管理器


class submsgAdmin(object):
    list_display = [
        'name',
        'topic',
        'subtime',
        "payload"]
    search_fields = [
        'name',
        'topic',
        ]
    list_filter = [
        'name',
        'topic',
        ]
    model_icon = 'fa fa-feed'


# 将管理器与model进行注册关联
xadmin.site.register(submsg, submsgAdmin)

