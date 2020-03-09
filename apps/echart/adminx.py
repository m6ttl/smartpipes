# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import ewsales
import xadmin

# ewPresales的admin管理器


class ewsalesAdmin(object):
    list_display = [
        'name',
        'owner',
        'typen',
        'builder',
        'builder_date',
        'dept',
        'province',
        'city',
        'prj_name',
        'status',
        'order_m']
    search_fields = [
        'name',
        'owner',
        'typen',
        'builder',
        'province']
    list_filter = [
        'name',
        'owner',
        'typen',
        'dept',
        'city']

# 将管理器与model进行注册关联
xadmin.site.register(ewsales, ewsalesAdmin)