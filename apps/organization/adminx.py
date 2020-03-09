# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 21:21'

import xadmin

from .models import CityDict, CourseOrg, Teacher


# 类型所属分类名后台管理器
class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    model_icon = 'fa fa-cube'


# 类型课程信息管理器
class CourseOrgAdmin(object):
    list_display = ['name', 'desc','category',  'click_nums', 'fav_nums','add_time' ]
    search_fields = ['name', 'desc','category',  'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'category', 'click_nums', 'fav_nums','city__name','address','add_time']
    model_icon = 'fa fa-database'


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company','email','add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org__name', 'name', 'work_years', 'work_company','click_nums', 'fav_nums', 'add_time']
    model_icon = 'fa fa-check'


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
