# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import ewsales, wxmsg
import xadmin

# ewPresales的admin管理器


class ewsalesAdmin(object):
    list_display = [
        'name',
        'owner',
        'typen',
        'builder',
        'builder_date',
        'dept',
        'province',
        'city',
        'prj_name',
        'status',
        'order_m']
    search_fields = [
        'name',
        'owner',
        'typen',
        'builder',
        'province']
    list_filter = [
        'name',
        'owner',
        'typen',
        'dept',
        'city']



class wxmsgAdmin(object):
    list_display = [
        'name',
        'rank',
        'to_type',
        'to_man',
        'builder',
        'builder_date',
        'msg',
        'send_flag',
        'ans_status',
        'effect_b',
        'effect_e',
        'area']
    search_fields = [
        'name',
        'to_type',
        'to_man',
        'msg',
        'send_flag',
        'ans_status']
    list_filter = [
        'name',
        'to_type',
        'to_man',
        'msg',
        'send_flag',
        'ans_status']


# class ewProjectAdmin(object):
#     list_display = [
#         # 月份    任务单编号    项目名称    项目所属    分项类型    项目分类 项目合同金额
#         '月份',
#         'p_id',
#         '项目名称',
#         '所属',
#         '大类',
#         '分项',
#         '分类',
#         '合同金额']
#     search_fields = [
#         '月份']
#     list_filter = [
#         '月份']

# 将管理器与model进行注册关联
xadmin.site.register(ewsales, ewsalesAdmin)
xadmin.site.register(wxmsg, wxmsgAdmin)
# xadmin.site.register(ewsales, ewProjectAdmin)
