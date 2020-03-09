# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import Course, Lesson, Video, CourseResource, MyCourse
import xadmin
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db.models import Q

# Course的admin管理器

class LessonInline(object):
    model = Lesson
    extra = 0

class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'degree',
        'learn_times',
        'teacher',
        # 'get_email',
        'students']
    search_fields = ['name', 'desc', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'degree',
        'teacher',
        'learn_times',
        'students']
    # 富文本
    style_fields = {"detail": "ueditor"}
    model_icon = 'fa fa-university'

    def queryset(self):
        if not self.request.user.is_superuser:  # 用户可查看自己的文章
            qs = super(CourseAdmin, self).queryset()
            qs = qs.filter(Q(teacher__email=self.request.user.email) | Q(email=self.request.user.email))
        else: # 超级用户可查看所有数据
            qs = super(CourseAdmin, self).queryset()
        return qs

    def save_models(self):
        self.new_obj.email = self.request.user.email
        super().save_models()

# 自己发的课程
class MyCourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'degree',
        'category',
        'learn_times',
        'get_email',
        'students']
    search_fields = ['name', 'desc', 'degree', 'students']
    list_filter = [
        'name',
        'desc',
        'degree',
        'learn_times',
        'students']
    # 富文本
    style_fields = {"detail": "ueditor"}
    readonly_fields = ['email']

    # inlines = [LessonInline, CourseResourceInline]

    # style_fields = {"Lessondetail": "ueditor"}
    model_icon = 'fa fa-book'

    def queryset(self):
        qs = super(MyCourseAdmin, self).queryset()
        # qs = qs.filter( teacher__email=self.request.user.email )
        qs = qs.filter( Q(teacher__email=self.request.user.email) | Q(email=self.request.user.email))

        return qs

    def save_models(self):
        self.new_obj.email = self.request.user.email
        super().save_models()

class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']
    style_fields = {"Lessondetail": "ueditor"}
    list_editable = [ 'name']
    ordering = [ 'name']
    model_icon = 'fa fa-book'

    def queryset(self):
        if not self.request.user.is_superuser:  # 用户可查看自己的文章
            qs = super(LessonAdmin, self).queryset()
            # qs = qs.filter(course__name_)
            qs = qs.filter(Q(course__teacher__email=self.request.user.email) | Q(course__email=self.request.user.email))
        else: # 超级用户可查看所有数据
            qs = super(LessonAdmin, self).queryset()
        return qs

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']

    model_icon = 'fa fa-caret-square-o-right'
    def queryset(self):
        if not self.request.user.is_superuser:  # 用户可查看自己的文章
            qs = super(VideoAdmin, self).queryset()
            # qs = qs.filter(course__name_)
            qs = qs.filter(Q(lesson__course__teacher__email=self.request.user.email) | Q(lesson__course__email=self.request.user.email))
        else: # 超级用户可查看所有数据
            qs = super(VideoAdmin, self).queryset()
        return qs

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download', 'add_time']

    model_icon = 'fa fa-briefcase'

    def queryset(self):
        if not self.request.user.is_superuser:  # 用户可查看自己的文章
            qs = super(CourseResourceAdmin, self).queryset()
            # qs = qs.filter(course__name_)
            qs = qs.filter(Q(course__teacher__email=self.request.user.email) | Q(course__email=self.request.user.email))
        else: # 超级用户可查看所有数据
            qs = super(CourseResourceAdmin, self).queryset()
        return qs

# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(MyCourse, MyCourseAdmin)
