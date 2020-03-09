# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import scenhtml, scenResource
from django.db.models import Q

import xadmin

# ewPresales的admin管理器

#应用场景
class scenhtmlAdmin(object):
    list_display = [
        'name',
        'typen',
        'builder'
    ]
    # fields  = [
    #     'name',
    #     'typen',
    #     'title'
    # ]


    search_fields = [
        'name',
        'typen',
        'builder']
    list_filter = [
        'name',
        'typen',
        'builder']
    model_icon = 'fa fa-bullhorn'

    def save_models(self):
        self.new_obj.builder = self.request.user.nick_name
        super().save_models()


#提交报告文档
class scenResourceAdmin(object):
    list_display = ['project', 'name', 'download', 'add_time', ]
    search_fields = ['project', 'name', 'download']
    list_filter = ['project__name', 'name', 'download', 'add_time']
    ordering = ('-add_time',)

    model_icon = 'fa fa-briefcase'

# # 用户报告阅读表
# class ReportUserAdmin(object):
#     list_display = ['user', 'report', 'add_time']
#     search_fields = ['user', 'report']
#     list_filter = ['user', 'report', 'add_time']

xadmin.site.register(scenhtml, scenhtmlAdmin)
xadmin.site.register(scenResource, scenResourceAdmin)
# xadmin.site.register(ReportUser, ReportUserAdmin)


