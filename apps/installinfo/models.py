# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


class installinfo(models.Model):
    ### 安装信息
    name = models.CharField(max_length=64, verbose_name=u"消息名称", blank=True, null=True)
    caliber = models.CharField(max_length=64, verbose_name=u"口径", blank=True, null=True)
    sn = models.DateTimeField(max_length=40, verbose_name=u"编号", blank=True, null=True)
    RTU_id = models.TextField(max_length=100, verbose_name=u"RTU编号", blank=True, null=True)
    depth = models.TextField(max_length=20, verbose_name=u"埋深", blank=True, null=True)
    install_date = models.TextField(default=datetime.now, verbose_name=u"安装时间", blank=True, null=True)
    interface = models.TextField(max_length=50, verbose_name=u"接口方式", blank=True, null=True)
    pipeline = models.TextField(max_length=50, verbose_name=u"管道材质", blank=True, null=True)
    longitude = models.TextField(max_length=50, verbose_name=u"安装经度", blank=True, null=True)
    latitude = models.TextField(max_length=50, verbose_name=u"安装纬度", blank=True, null=True)

    class Meta:
        verbose_name = u"安装信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
