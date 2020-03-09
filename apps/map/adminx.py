# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import gis_info
from xadmin import views
import xadmin

# ewPresales的admin管理器

# # 自定义菜单
# class GlobalSettings(object):
#
#     def get_site_menu(self):
#         return [
#             {'title': '统计分析',
#                  'perm': self.get_model_perm(Service, 'view'),
#                  'icon':'fa fa-gg',
#                  'menus': (
#                     {'title': '百度',
#                       'url': 'hrrp://www.baidu.com',
#                       'perm': self.get_model_perm(Service, 'view')
#                     },
#                     {'title': 'google',
#                      'url': 'hrrp://www.google.com',
#                      'perm': self.get_model_perm(Service, 'view')
#                      },
#                  )
#             },
#         ]

class gis_infoAdmin(object):
    list_display = [
        'id',
        'proj_id',
        'name',
        'p_type',
        'lon',
        'lat']
    search_fields = [
        'proj_id',
        'name',
        'p_type',]
    list_filter = [
        'proj_id',
        'name',
        'p_type',]

    model_icon = 'fa fa-film'


# 将管理器与model进行注册关联
xadmin.site.register(gis_info, gis_infoAdmin)

# xadmin.site.register(views.CommAdminView, GlobalSettings)

