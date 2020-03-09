# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import ewPresales
import xadmin

# ewPresales的admin管理器


class ewPresalesAdmin(object):
    list_display = [
        'name',
        'owner',
        'typen',
        'builder',
        'builder_date',
        'modi_man',
        'modi_date',
        'dept',
        'prj_name',
        'need_finish_date',
        'flow_n',
        'feedback',
        'typen',
        'status',
        'mayer_word',
        'do_s',
        'presales_man',
        'presales_plan']
    search_fields = [
        'name',
        'owner',
        'typen',
        'builder',
        'presales_man']
    list_filter = [
        'name',
        'owner',
        'typen',
        'builder',
        'presales_man']

# 将管理器与model进行注册关联
xadmin.site.register(ewPresales, ewPresalesAdmin)