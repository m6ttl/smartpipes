# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

class gis_info(models.Model):
    proj_id = models.CharField(max_length=100, verbose_name=u"项目")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    p_type = models.CharField(max_length=10, verbose_name=u"类型", blank=True, null=True)
    lon = models.FloatField( verbose_name=u"经度", blank=True, null=True)
    lat = models.FloatField(verbose_name=u"纬度", blank=True, null=True)

    class Meta:
        verbose_name = u"地图信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name