# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import  xxProject, xxProjectResource, xxProjectChange, xxProjectComments
from .models import   xxProjectResourceInline, xxProjectCommentsInline, xxProjectChangeInline, xxProjectB
from django.db.models import Q

import xadmin

# xxPresales的admin管理器


#聚联项目
class xxProjectAdmin(object):
    list_display = [
        'name',
        'xxsales',
        'EWsales',
        'p_stage',
        'province',
        'city',
        'get_zy_nums',
        'get_jl_nums',
        # 'id',
        'p_month',
        'budget_m',
        'p_org',
        'total_pr',
        'start_cond',
        'start_month',
        'next_memo'
    ]
    # list_editable = [
    #     'total_pr'
    # ]
    ordering = ('-id',)
    search_fields = [
        'province',
        'city',
        'p_org',
        'p_stage',
        'total_pr',
        'next_memo'
    ]
    list_filter = [
        'province',
        'city',
        'p_org',
        'p_stage',
        'total_pr',
        'next_memo'
    ]

    # inlines = [xxProjectResourceInline, xxProjectChangeInline, xxProjectCommentsInline]
    # inlines = [ xxProjectResourceInline, xxProjectCommentsInline, xxProjectChangeInline]

    model_icon = 'fa fa-arrows-alt'


#项目变更记录
class xxProjectChangeAdmin(object):
    list_display = ['project', 'name', 'kind','c_date']
    search_fields = ['project','name', 'kind']
    list_filter = ['project__name', 'name', 'name', 'kind']
    ordering = ('-c_date',)

    model_icon = 'fa fa-share'



# 项目资源
class xxProjectResourceAdmin(object):
    list_display = ['project', 'name', 'download', 'add_time', ]
    search_fields = ['project', 'name', 'download']
    list_filter = ['project__name', 'name', 'download', 'add_time']
    ordering = ('-add_time',)

    model_icon = 'fa fa-book'


# 项目交流
class xxProjectCommentsAdmin(object):
    list_display = ['course', 'user','kind','ctitle','comments', 'add_time' ]
    search_fields = ['course' 'user','kind','ctitle']
    list_filter = ['course',  'user','kind','ctitle']
    readonly = ['user']
    ordering = ('-add_time',)

    # def save_models(self):
    #     self.new_obj.user = self.request.user
    #     super().save_models()
    def save_model(self):
        obj = self.new_obj
        obj.user = self.request.User
        obj.save()
    model_icon = 'fa fa-hand-o-left'



#聚联项目浏览
class xxProjectBAdmin(object):
    list_display = [
        'name',
        # 'id',
        # 'p_month',
        # 'province',
        'city',
        # 'name',
        # 'budget_m',
        'xxsales',
        'EWsales',
        # 'p_org',
        'p_stage',
        # 'total_pr',
        # 'start_cond',
        # 'start_month',
        # 'next_memo'
    ]
    # list_editable = [
    #     'total_pr'
    # ]
    ordering = ('-id',)
    search_fields = [
        'province',
        'city',
        'p_org',
        'p_stage',
        'total_pr',
        'next_memo'
    ]
    list_filter = [
        'province',
        'city',
        'p_org',
        'p_stage',
        'total_pr',
        'next_memo'
    ]

    # inlines = [xxProjectResourceInline, xxProjectChangeInline, xxProjectCommentsInline]
    inlines = [ xxProjectResourceInline, xxProjectCommentsInline, xxProjectChangeInline]
    # def save_model(self):
    #     obj = self.new_obj
    #     obj.xxProjectCommentsInline.user = self.request.User
    #     obj.xxProjectCommentsInline.save()

    model_icon = 'fa fa-user-plus'

# 将管理器与model进行注册关联
# xadmin.site.register(xxPresales, xxPresalesAdmin)
xadmin.site.register(xxProject, xxProjectAdmin)
xadmin.site.register(xxProjectResource, xxProjectResourceAdmin)
xadmin.site.register(xxProjectChange, xxProjectChangeAdmin)
xadmin.site.register(xxProjectComments, xxProjectCommentsAdmin)

xadmin.site.register(xxProjectB, xxProjectBAdmin)

