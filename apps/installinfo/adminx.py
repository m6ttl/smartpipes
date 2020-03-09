# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import installinfo


import xadmin

# ewPresales的admin管理器


class installinfoAdmin(object):
    list_display = [
        'name',
        'caliber',
        'sn',
        "RTU_id",
        "depth",
        "install_date",
        "interface",
        "pipeline",
        "longitude",
        "latitude"]
    search_fields = [
        'name',
        'caliber',
        'sn',
        "RTU_id",
        "depth",
        "interface",
        "pipeline",
        "longitude",
        "latitude"
        ]
    list_filter = [
        'name',
        'caliber',
        'sn',
        "RTU_id",
        "depth",
        "install_date",
        "interface",
        "pipeline",
        "longitude",
        "latitude"
        ]
    model_icon = 'fa fa-deaf'


# 将管理器与model进行注册关联
xadmin.site.register(installinfo, installinfoAdmin)

