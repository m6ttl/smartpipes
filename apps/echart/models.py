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
    order_m = models.FloatField( verbose_name=u"金额", blank=0, null=True)

    class Meta:
        verbose_name = u"销售合同"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name