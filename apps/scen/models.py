# encoding: utf-8

from datetime import datetime
import time
from django.db import models
from django.db.models import Sum,Count,Max,Min,Avg

from users.models import UserProfile

from DjangoUeditor.models import UEditorField

# Create your models here.

def get_kargs(**kwargs):
    return kwargs


# 字符串时间转换函数
def to_date(datetime1, format_date):
    Normaltime = datetime.datetime.strptime(datetime1, format_date)
    return Normaltime


# datetime时间转为字符串
def to_char(datetime1, format_ymd):
    str1 = datetime1.strftime(format_ymd)
    return str1


# datetime时间转为时间戳
def date_to_datetamp(dt1):
    Unixtime = time.mktime(time.strptime(dt1.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'))
    return Unixtime


# 时间戳转为datetime时间
def datetamp_to_date(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt


# 多久之前 （传入时间戳）
def date_go(t):
    delta = int(time.time() - t)
    if delta < 60:
        return '刚才'
    if delta < 60 * 60:
        return '%s分钟前' % (delta // 60)
    if delta < 60 * 60 * 24:
        return '%s小时前' % (delta // (60 * 60))
    if delta < 60 * 60 * 24 * 31:
        return '%s天前' % (delta // (60 * 60 * 24))
    if delta < 60 * 60 * 24 * 365:
        return '%s月前' % (delta // (60 * 60 * 24 * 31))
    return '%s年前' % (delta // (60 * 60 * 24 * 365))


    #业务报告
class scenhtml(models.Model):
    RPT_CHOICES = (
        (u"水务", u"水务"),
        (u"水利", u"水利")
    )
    name = models.CharField(max_length=100, verbose_name=u"名称")
    typen = models.CharField(max_length=30, choices=RPT_CHOICES, verbose_name=u"场景类型", blank=True, null=True)
    builder = models.CharField(max_length=10, verbose_name=u"创建人", blank=True, null=True)
    build_date = models.DateTimeField(verbose_name=u"上传时间", default=datetime.now, blank=True, null=True)
    download = models.FileField(
        upload_to="scen",
        verbose_name=u"应用场景",
        max_length=100)

    # download = models.JupyterFileField(
    #     upload_to="course/resource/%Y/%m",
    #     verbose_name=u"HTML报告",
    #     max_length=100)

    def get_day_go(self):
        # 获取课程交流数的方法
        return date_go(date_to_datetamp(self.build_date))
    get_day_go.short_description = '发布时间'

    # 获取学习这门报告的用户
    # 替代标签:course.usercourse_set.get_queryset|slice:":1"
    # def get_learn_users(self):
    # #     # 谁的里面添加了它做外键，他都可以取出来
    #     return self.reportuser_set.all()[:5]

    class Meta:
        verbose_name = u"应用场景"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

# 报告附件
class scenResource(models.Model):
    # 因为一个项目对应很多资源。所以在项目资源表中将项目设置为外键。
    # 作为一个字段来让我们可以知道这个资源对应那个项目
    project = models.ForeignKey(scenhtml, on_delete=models.CASCADE, verbose_name=u"场景")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        # upload_to="course/resource/%Y/%m",
        upload_to="scen/resource",
        verbose_name=u"资源文件",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"场景附件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》场景的资源: {1}'.format(self.project,self.name)

# # 用户报告阅读表
# class ReportUser(models.Model):
#     # 会涉及两个外键: 1. 用户， 2. 场景。import进来
#     report = models.ForeignKey(scenhtml, on_delete=models.CASCADE, verbose_name=u"场景")
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name=u"阅读时间")
#
#     class Meta:
#         verbose_name = u"报告阅读用用户"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return '用户({0})阅读了{1} '.format(self.user, self.report)