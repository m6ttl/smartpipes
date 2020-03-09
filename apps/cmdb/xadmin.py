# import xadmin
# from .models import User, Entry
#
#
# class UserAdmin(object):
#     # 需要显示的字段
#     list_display = ('name', 'email')
#
#
# class EntryAdmin(object):
#     list_display = ('title', 'body', 'created_at', 'updated_at', 'status', 'author')
#
#
# xadmin.site.register(User, UserAdmin)
# xadmin.site.register(Entry, EntryAdmin)


# _*_ coding: utf-8 _*_

import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(views.BaseAdminView,BaseSetting)


# class GlobalSettings(object):
#     site_title="ewide后台管理系统"
#     site_footer="steveWei"
#     menu_style="accordion"
# xadmin.site.register(views.CommAdminView,GlobalSettings)