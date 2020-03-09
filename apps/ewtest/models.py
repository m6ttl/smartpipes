# encoding: utf-8

from datetime import datetime
from django.db import models

from DjangoUeditor.models import UEditorField

# Create your models here.

# 售前任务单


class ewPresales(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"名称")
    owner = models.CharField(max_length=20, verbose_name=u"所有人", blank=True, null=True)
    typen = models.CharField(max_length=20, verbose_name=u"业务类型", blank=True, null=True)
    builder = models.CharField(max_length=10, verbose_name=u"创建人", blank=True, null=True)
    builder_date = models.DateTimeField(blank=True, verbose_name=u"创建日期", null=True)
    modi_man = models.CharField(max_length=10, verbose_name=u"修改人", blank=True, null=True)
    modi_date = models.DateTimeField(blank=True, verbose_name=u"修改日期", null=True)
    dept = models.CharField(max_length=40, verbose_name=u"所属部门", blank=True, null=True)
    prj_name = models.CharField(max_length=100, verbose_name=u"销售机会名称", blank=True, null=True)
    need_finish_date = models.DateTimeField(blank=True, verbose_name=u"要求完成时间", null=True)
    flow_n = models.CharField(max_length=30, verbose_name=u"工作流阶段名称", blank=True, null=True)
    feedback = models.CharField(max_length=40, verbose_name=u"完成效果反馈", blank=True, null=True)
    status = models.CharField(max_length=30, verbose_name=u"售前任务单状态", blank=True, null=True)
    mayer_word = models.CharField(max_length=100, verbose_name=u"售前主要工作", blank=True, null=True)
    do_s = models.CharField(max_length=40, verbose_name=u"审批状态", blank=True, null=True)
    presales_man = models.CharField(max_length=100, verbose_name=u"售前负责人", blank=True, null=True)
    presales_plan = models.CharField(max_length=4096, verbose_name=u"本次售前策略", blank=True, null=True)
    m1 = models.CharField(max_length=10, blank=True, null=True)
    m2 = models.CharField(max_length=10, blank=True, null=True)
    m3 = models.CharField(max_length=10, blank=True, null=True)
    m4 = models.CharField(max_length=10, blank=True, null=True)
    m5 = models.CharField(max_length=10, blank=True, null=True)
    m6 = models.CharField(max_length=10, blank=True, null=True)
    m7 = models.CharField(max_length=10, blank=True, null=True)
    m8 = models.CharField(max_length=10, blank=True, null=True)
    m9 = models.CharField(max_length=10, blank=True, null=True)
    m10 = models.CharField(max_length=10, blank=True, null=True)
    n1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    n2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    n3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    n4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    n5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    n6 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    n7 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    n8 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = u"售前任务单"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name