# encoding: utf-8

from datetime import datetime
from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.

# 销售合同


class ewsales(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"名称")
    owner = models.CharField(max_length=20, verbose_name=u"所有人", blank=True, null=True)
    typen = models.CharField(max_length=20, verbose_name=u"业务类型", blank=True, null=True)
    builder = models.CharField(max_length=10, verbose_name=u"创建人", blank=True, null=True)
    builder_date = models.DateTimeField(blank=True, verbose_name=u"签约日期", null=True)
    dept = models.CharField(max_length=40, verbose_name=u"所属部门", blank=True, null=True)
    province = models.CharField(max_length=20, verbose_name=u"省份", blank=True, null=True)
    city = models.CharField(max_length=20, verbose_name=u"城市", blank=True, null=True)
    prj_name = models.CharField(max_length=100, verbose_name=u"客户名", blank=True, null=True)
    status = models.CharField(max_length=30, verbose_name=u"完成状态", blank=True, null=True)
    order_m = models.DecimalField(verbose_name=u"金额", max_digits=12, decimal_places=2)
    attachfile = models.FileField(upload_to='upload',default = '')

    class Meta:
        verbose_name = u"销售合同"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#微信自动任务表

class wxmsg(models.Model):
    TO_CHOICES = (
        ("0", u"微信好友"),
        ("1", u"项目经理群"),
        ("2", u"知识专家群"),
        ("3", u"测试群")
    )
    name = models.CharField(max_length=40, verbose_name=u"标题", blank=True, null=True)
    rank = models.IntegerField(default=0, verbose_name = u"优先级别", blank=True, null=True)
    to_type = models.CharField(max_length=20, verbose_name=u"发送类型", blank=True, null=True)
    to_man = models.CharField(max_length=40, verbose_name=u"责任人", blank=True, null=True)
    builder = models.CharField(max_length=20, verbose_name=u"创建人", blank=True, null=True)
    builder_date = models.DateTimeField(blank=True, verbose_name=u"创建日期", null=True)
    msg = models.CharField(max_length=1024, verbose_name=u"内容", blank=True, null=True)
    send_flag = models.IntegerField(default=0, verbose_name=u"发出标志", blank=True, null=True)
    ans_status = models.IntegerField(default=0, verbose_name=u"回复标志", blank=True, null=True)
    effect_b = models.DateTimeField( verbose_name=u"生效起始时间", blank=True, null=True)
    effect_e = models.DateTimeField( verbose_name=u"生效截止时间", blank=True, null=True)
    area = models.CharField(max_length=20, verbose_name=u"发送范围类型", blank=True, null=True)

    class Meta:
        verbose_name = u"微信自动任务"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name






