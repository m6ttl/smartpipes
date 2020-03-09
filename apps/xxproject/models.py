# encoding: utf-8

from datetime import datetime
import time
from django.db import models
from django.db.models import Sum,Count,Max,Min,Avg
from django.contrib.auth.models import User

from users.models import UserProfile

from DjangoUeditor.models import UEditorField

# Create your models here.

# class Kuaijian(models.Model):
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE)

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


#聚联项目
class xxProject(models.Model):
    ORG_CHOICES = (
        (u"产销差",u"产销差"),
        (u"智慧水务",u"智慧水务"),
        (u"三供一业",u"三供一业"),
        (u"营销",u"营销"),
        (u"供水",u"供水"),
        (u"水利",u"水利"),
        (u"排水", u"排水"),
        (u"服务",u"服务")
    )
    STAGE_CHOICES = (
        (u"设想", u"设想"),
        (u"立项", u"立项"),
        (u"招采", u"招采"),
        (u"施工", u"施工"),
        (u"暂停", u"暂停"),
        (u"取消", u"取消")
    )
    p_month = models.CharField(max_length=10, verbose_name=u"消息月份", default='2019/01')
    p_date = models.DateField(verbose_name=u"任务单时间", blank=True, null=True)

    province = models.CharField(max_length=20, verbose_name=u"省", null=True, blank=True)
    city = models.CharField(max_length=20, verbose_name=u"地名", null=True, blank=True)
    area_rank = models.CharField(max_length=20, verbose_name=u"级别", default='市', null=True, blank=True)

    name = models.CharField(max_length=128, verbose_name=u"项目名称")
    budget_m = models.IntegerField(default=0, verbose_name=u"预计金额", blank=True, null=True)


    xxsales = models.CharField(max_length=20, verbose_name=u"新兴销售人员", blank=True, null=True)
    EWsales = models.CharField(max_length=20, verbose_name=u"易维对接人", blank=True, null=True)

    p_org = models.CharField(choices=ORG_CHOICES, max_length=40, verbose_name=u"大类", blank=True, null=True)
    p_stage = models.CharField(choices=STAGE_CHOICES, max_length=40, verbose_name=u"阶段", blank=True, null=True)

    total_pr = models.IntegerField(default=0, verbose_name=u"概率", blank=True, null=True)

    start_cond = models.CharField(max_length=128, verbose_name=u"启动前置条件", blank=True, null=True)
    start_month = models.DateField(verbose_name=u"计划开始日期", blank=True, null=True)

    p_memo = UEditorField(verbose_name=u"项目信息", width=600, height=100, imagePath="courses/ueditor/",
                      filePath="courses/ueditor/", blank=True, null=True)

    finish_memo = UEditorField(verbose_name=u"已完成工作", width=600, height=100, imagePath="courses/ueditor/",
                           filePath="courses/ueditor/", blank=True, null=True)

    next_memo = UEditorField(verbose_name=u"下一步工作", width=600, height=100, imagePath="courses/ueditor/",
                         filePath="courses/ueditor/", blank=True, null=True)
    class Meta:
        verbose_name = u"聚联项目清单"
        verbose_name_plural = verbose_name

    def get_zy_nums(self):
        # 获取附件数的方法
        return self.xxProjectResource_set.all().count()
    get_zy_nums.short_description = '附件'

    def get_jl_nums(self):
        # 获取交流数的方法
        # return self.xxProjectComments_set__count
        return self.xxProjectComments_set.all().count()
    get_jl_nums.short_description = '交流'

    def __str__(self):
        return self.name

class xxProjectB(xxProject):
    class Meta:
        verbose_name = '聚联项目手机浏览'
        verbose_name_plural = verbose_name
        #这里必须设置proxy=True，这样就不会再生成一张表，同时还具有Model的功能
        proxy = True

# 项目资源
class xxProjectResource(models.Model):
    # 因为一个项目对应很多资源。所以在项目资源表中将项目设置为外键。
    # 作为一个字段来让我们可以知道这个资源对应那个项目
    project = models.ForeignKey(xxProject, on_delete=models.CASCADE, verbose_name=u"项目")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"项目资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》项目的资源: {1}'.format(self.project,self.name)

class xxProjectResourceInline(object):
    model = xxProjectResource
    extra = 0

# 项目变更日志
class xxProjectChange(models.Model):
    project = models.ForeignKey(xxProject, on_delete=models.CASCADE, verbose_name=u"项目")
    name = models.CharField(max_length=100, verbose_name=u"变更内容")
    kind = models.CharField(max_length=40, verbose_name=u"类型", blank=True, null=True)
    old = models.CharField(max_length=40, verbose_name=u"原值", blank=True, null=True)
    new = models.CharField(max_length=40, verbose_name=u"现值", blank=True, null=True)
    c_date = models.DateField(default=datetime.now, verbose_name=u"变更时间", blank=True, null=False)

    class Meta:
        verbose_name = u"项目重要变更"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '[{1}] 日 [{2}] : {3}'.format(self.project,to_char(self.c_date, '%Y-%m-%d'),self.kind, self.name)

class xxProjectChangeInline(object):
    model = xxProjectChange
    list_display = ['name',]
    exclude = ['name','c_date','kind','kind','old','new']
    extra = 0
    class Meta:
        verbose_name = u"变更"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》变更[{1}]: {2}'.format(date_go(self.c_date), self.kind, self.name)


# 对于新兴项目交流
class xxProjectComments(models.Model):
    CM_CHOICES = (
        ("pl", u"评论"),
        ("rw", u"任务"),
        ("zx", u"咨询"),
        ("jl", u"建议")
    )
    # 会涉及两个外键: 1. 用户， 2. 新兴项目 。import进来
    course = models.ForeignKey(xxProject, on_delete=models.CASCADE, verbose_name=u"项目")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户",default = '')

    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=u"用户")

    # comments = models.CharField(max_length=250, verbose_name=u"交流")

    kind = models.CharField(choices=CM_CHOICES, max_length=2, verbose_name=u"类型", default = 'pl')
    ctitle = models.CharField(max_length=30, verbose_name="主题", default = '交流')
    comments = UEditorField(verbose_name=u"交流")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"提交时间")

    class Meta:
        verbose_name = u"项目交流"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对[{1}] 提出评论:'.format(self.user, self.course)

class xxProjectCommentsInline(object):
    model = xxProjectComments
    exclude = ['course','add_time']
    # fields = ['ctitle','comments']
    readonly = ['user']

    extra = 0
    def save_model(self):
        obj = self.new_obj
        obj.user = self.request.User.id
        obj.save()
    def __str__(self):
        return '用户({0})于[{1}],提出《{2}》 评论 :'.format(to_char(self.user), self.add_time, self.kind)


# # 项目回款记录
# class ProjectReceived(models.Model):
#     REC_CHOICES = (
#         (u"首付款", u"首付款"),
#         (u"启动款", u"启动款"),
#         (u"上线款", u"上线款"),
#         (u"验收款", u"验收款"),
#         (u"质保款", u"质保款")
#     )
#     project = models.ForeignKey(ewProject, on_delete=models.CASCADE, verbose_name=u"项目")
#     p_month = models.CharField(max_length=20, verbose_name=u"月份", null=False, default = '2019/01')
#     kind = models.CharField(choices=REC_CHOICES, max_length=40, verbose_name=u"类型", blank=True, null=True)
#     builder = models.CharField(max_length=10, verbose_name=u"登记人", blank=True, null=True)
#     build_date = models.DateField(verbose_name=u"发生日期", default=datetime.now, blank=True, null=True)
#     pay = models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=False, verbose_name='金额')
#
#     class Meta:
#         verbose_name = u"项目回款"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return '《{0}》项目的项目回款: {1}'.format(self.project, self.kind)
#
#
# #项目采购记录
# class ProjectPay(models.Model):
#     project = models.ForeignKey(ewProject, on_delete=models.CASCADE, verbose_name=u"项目")
#     builder = models.CharField(max_length=10, verbose_name=u"经办人", blank=True, null=True)
#     build_date = models.DateField(verbose_name=u"日期", default=datetime.now, blank=True, null=True)
#     pay_id = models.CharField(max_length=40, verbose_name=u"申请单号", blank=True, null=True)
#     name = models.CharField(max_length=100, verbose_name=u"名称")
#     script = models.CharField(max_length=100, verbose_name=u"型号")
#     kind = models.CharField(max_length=100, verbose_name=u"付款描述", blank=True, null=True)
#     dept = models.CharField(max_length=40, verbose_name=u"部门", blank=True, null=True)
#     vendor = models.CharField(max_length=100, verbose_name=u"供应商")
#     qty =  models.IntegerField(default=0, verbose_name = u"数量", blank=True, null=True)
#     price = models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='单价'),
#     pay = models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=False, verbose_name='总金额')
#
#     class Meta:
#         verbose_name = u"项目采购"
#         verbose_name_plural = verbose_name
#
#
#     def __str__(self):
#         return '《{0}》项目的采购: {1}'.format(self.project, self.name)
#
# #验收信息
# class ewProjectCheck(ewProject):
#     class Meta:
#         verbose_name = u"验收信息"
#         verbose_name_plural = verbose_name
#         proxy = True #必须这么些不会要求 migrite

