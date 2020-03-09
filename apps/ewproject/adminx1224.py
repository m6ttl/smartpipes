# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import ewPresales, ewProject, ewReport, ewProjectBackup, ewProjectCheck
import xadmin

# ewPresales的admin管理器

#售前工作单
class ewPresalesAdmin(object):
    list_display = [
        'name',
        'owner',
        'typen',
        'builder',
        'builder_date',
        'modi_man',
        'modi_date',
        'dept',
        'prj_name',
        'need_finish_date',
        'flow_n',
        'feedback',
        'typen',
        'status',
        'mayer_word',
        'do_s',
        'presales_man',
        'presales_plan']
    search_fields = [
        'name',
        'owner',
        'typen',
        'builder',
        'presales_man']
    list_filter = [
        'name',
        'owner',
        'typen',
        'builder',
        'presales_man']

#项目监管过程信息
class ewProjectAdmin(object):
    list_display = [
        'p_id',
        'p_month',
        'name',
        'province',
        'city',
        'sales',
        'p_dept',
        'p_pm',
        'p_org',
        'p_type',
        'p_kind',
        'bargain_m',
        'task_m',
        'p_status',
        'p_task_m',
        'p_project_m',
        'c_chk_date'
    ]
    list_editable = [
        'province',
        'city',
        'p_dept',
        'p_pm',
        'p_org',
        'p_type',
        'p_kind',
        'p_status',
        'p_task_m',
        'p_project_m'
    ]

    search_fields = [
        'p_id',
        'p_month',
        'name',
        'province',
        'city',
        'sales',
        'p_dept',
        'p_pm',
        'p_org',
        'p_type',
        'p_kind',
        'p_status',
        'bargain_m',
        'task_m']
    list_filter = [
        'p_id',
        'p_month',
        'name',
        'province',
        'city',
        'sales',
        'p_dept',
        'p_org',
        'p_type',
        'p_kind',
        'p_status',
        'bargain_m',
        'task_m']


#项目立项信息

#验收信息
class ewProjectModiAdmin(object):
    list_display = [
        'p_id',
        'p_month',
        'name',
        'c_code_backup_date',
        'c_database_backup_date',
        'city',
        'p_dept']
    search_fields = ['p_id', 'p_month', 'name', 'city', 'p_dept']
    list_filter = [
        'p_id',
        'p_month',
        'name',
        'city',
        'p_dept']
    list_editable = ['name','c_code_backup_date', 'c_database_backup_date']
    list_display_links = []

    # def has_delete_permission(self):
    #     return False
    #
    # def has_insert_permission(self):
    #     return False

    # def queryset(self):
    #     qs = super(ewProjectAdmin, self).queryset()
    #     return qs

#源码备份信息
class ewProjectBackupAdmin(object):
    list_display = [
        'p_id',
        'p_month',
        'name',
        'c_code_backup_date',
        'c_database_backup_date',
        'city',
        'p_dept']
    search_fields = ['p_id', 'p_month', 'name', 'city', 'p_dept']
    list_editable = ['c_code_backup_date', 'c_database_backup_date']
    readonly_fields  = [
        'p_id',
        'p_month',
        'name'
    ]
    list_filter = [
        'p_id',
        'p_month',
        'name',
        'city',
        'p_dept']
    fields  = [
        'p_id',
        'p_month',
        'name',
        'c_code_backup_date',
        'c_database_backup_date'
    ]
    # list_editable = ['name','c_code_backup_date', 'c_database_backup_date']
    # list_display_links = []

#验收信息
class ewProjectCheckAdmin(object):
    list_display = [
        'p_id',
        'p_month',
        'name',
        'city',
        'p_dept',
        'c_chk_date',
        'c_chk_man',
        'c_budget_m',
        'c_final_m',
        'c_diff_m',
        'c_cash_cost',
        'c_pay_cost',
        'c_use_date',
        'c_chk_date',
        'c_code_backup_date',
        'c_database_backup_date',
        'c_week',
        'c_week_report',
        'c_filechklist_c',
        'c_file_audit_c'
    ]
    search_fields = ['p_id', 'p_month', 'name', 'city', 'p_dept']
    readonly_fields  = [
        'p_id',
        'p_month',
        'name'
    ]
    list_filter = [
        'p_id',
        'p_month',
        'name',
        'city',
        'p_dept']
    fields  = [
        'p_id',
        'p_month',
        'name',
        'p_status',
        'p_pm',
        'c_chk_date',
        'c_chk_man',
        'c_budget_m',
        'c_final_m',
        'c_diff_m',
        'c_cash_cost',
        'c_pay_cost',
        'c_use_date',
        'c_chk_date',
        'c_code_backup_date',
        'c_database_backup_date',
        'c_week',
        'c_week_report',
        'c_filechklist_c',
        'c_file_audit_c',
        'c_file_memo',
    ]
    def queryset(self):
        qs = super(ewProjectCheckAdmin, self).queryset()
        # qs = qs.filter( teacher__email=self.request.user.email )
        qs = qs.filter(  p_status = '已验收')

        return qs


#提交报告
class ewReportAdmin(object):
    list_display = [
        'name',
        'typen',
        'builder',
        'title'
    ]
    fields  = [
        'name',
        'typen',
        'title'
    ]


    search_fields = [
        'name',
        'typen',
        'builder',
        'title']
    list_filter = [
        'name',
        'typen',
        'builder',
        'title']

# 将管理器与model进行注册关联
xadmin.site.register(ewPresales, ewPresalesAdmin)
xadmin.site.register(ewProject, ewProjectAdmin)
xadmin.site.register(ewReport, ewReportAdmin)
xadmin.site.register(ewProjectBackup, ewProjectBackupAdmin)
xadmin.site.register(ewProjectCheck, ewProjectCheckAdmin)
