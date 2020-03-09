# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

print('mqtt models')
class submsg(models.Model):
        ### 6、MQTT消息明细
    name = models.CharField(max_length=64, verbose_name=u"消息名称", blank=True, null=True)
    topic = models.CharField(max_length=64, verbose_name=u"主题", blank=True, null=True)
    subtime = models.DateTimeField(default=datetime.now, verbose_name=u"消息时间", blank=True, null=True)
    payload = models.TextField(max_length=500, verbose_name=u"消息内容", blank=True, null=True)

    class Meta:
        verbose_name = u"MQTT消息明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
