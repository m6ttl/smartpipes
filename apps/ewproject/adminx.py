# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import ewPresales, ewProject, ewReport,  ewProjectCheck, ReportResource, ReportUser
from .models import ProjectResource,  ProjectPay,ProjectReceived,ProjectChange
from django.db.models import Q

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
        'p_type',
        'p_kind',
        'p_begin_date',
        'bargain_m',
        'task_m',
        'p_s_use_date',
        'p_profit',
        'p_status'
    ]
    list_editable = [
        'province',
        'city',
        'p_dept',
        'p_pm',
        'p_dept',
        'p_type',
        'p_kind',
        'p_status'
    ]
    exclude= [
        'p_back_m',
        'p_back_scale',
        'p_task_m'
    ]
    ordering = ('-p_id',)
    search_fields = [
        'p_id',
        'p_month',
        'name',
        'province',
        'city',
        'sales',
        'p_dept',
        'p_pm',
        'p_type',
        'p_kind',
        'p_status',
        'bargain_m']
    list_filter = [
        'p_id',
        'p_month',
        'name',
        'province',
        'city',
        'sales',
        'p_dept',
        'p_type',
        'p_kind',
        'p_status',
        'bargain_m'
    ]


#验收信息
class ewProjectCheckAdmin(object):
    list_display = [
        'p_id',
        'p_month',
        'name',
        'city',
        'p_dept',
        'p_pm',
        'c_date',
        'c_cost_s',
        'c_file_s',
        'c_sched_s',
        'c_total_s',
        'c_delay_m',
        'p_profit'
    ]
    search_fields = ['p_id', 'p_month', 'name', 'city', 'p_dept']
    ordering = ('-p_id',)
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
        'city',
        'p_dept',
        'p_pm',

        'builder_date',
        'p_begin_date',
        'p_s_use_date',
        'c_real_chk_date',
        'c_delay_m',

        'c_sched_s',
        'task_m',

        'c_budget_m',
        'c_final_m',
        'c_diff_m',

        'c_m_project',
        'c_m_pay',
        'c_m_total',

        'p_project',
        'p_pay',
        'p_total',
        'p_profit',
        'p_project_scale',

        'c_cost_s',

        'p_plan_memo',
        'p_budget_memo',
        'c_filelist_memo',
        'c_file_memo',

        'c_week_s',
        'c_filechklist_s',
        'c_ys_s',
        'c_jh_s',
        'c_js_s',
        'c_ysb_s',
        'c_jj_s',
        'c_code_backup_s',
        'c_data_backup_s',
        'c_file_s',
        'c_total_s',
        'c_date',

        'c_filechklist_c',
        'c_ys_c',
        'c_jh_c',
        'c_js_c',
        'c_ysb_c',
        'c_jj_c',
        'c_code_backup_c',
        'c_week_report',
        'c_data_backup_c',

    ]
    def queryset(self):
        qs = super(ewProjectCheckAdmin, self).queryset()
        qs = qs.filter(p_status='已结案')

        return qs


#项目采购记录
class ProjectPayAdmin(object):
    list_display = ['project', 'name',  'script','kind','pay']
    search_fields = ['project', 'name',  'kind','pay']
    list_filter = ['project__name', 'name',  'kind','pay']
    ordering = ('-build_date',)

    model_icon = 'fa fa-briefcase'

#项目变更记录
class ProjectChangeAdmin(object):
    list_display = ['project', 'name', 'kind','c_date']
    search_fields = ['project','name', 'kind']
    list_filter = ['project__name', 'name', 'name', 'kind']
    ordering = ('-c_date',)

    model_icon = 'fa fa-briefcase'

# 项目资源
class ProjectResourceAdmin(object):
    list_display = ['project', 'name', 'download', 'add_time', ]
    search_fields = ['project', 'name', 'download']
    list_filter = ['project__name', 'name', 'download', 'add_time']
    ordering = ('-add_time',)

    model_icon = 'fa fa-briefcase'


# 回款记录
class ProjectReceivedAdmin(object):
    list_display = ['project', 'p_month', 'kind', 'pay']
    search_fields = ['project', 'p_month',   'kind', 'pay']
    list_filter = ['project__name', 'p_month',   'kind', 'pay']
    ordering = ('-build_date',)

    model_icon = 'fa fa-briefcase'

#提交报告
class ewReportAdmin(object):
    list_display = [
        'name',
        'typen',
        'builder'
    ]
    # fields  = [
    #     'name',
    #     'typen',
    #     'title'
    # ]


    search_fields = [
        'name',
        'typen',
        'builder']
    list_filter = [
        'name',
        'typen',
        'builder']

    def save_models(self):
        self.new_obj.builder = self.request.user.nick_name
        super().save_models()


#提交报告文档
class ReportResourceAdmin(object):
    list_display = ['project', 'name', 'download', 'add_time', ]
    search_fields = ['project', 'name', 'download']
    list_filter = ['project__name', 'name', 'download', 'add_time']
    ordering = ('-add_time',)

    model_icon = 'fa fa-briefcase'

# 用户报告阅读表
class ReportUserAdmin(object):
    list_display = ['user', 'report', 'add_time']
    search_fields = ['user', 'report']
    list_filter = ['user', 'report', 'add_time']


# 将管理器与model进行注册关联
# xadmin.site.register(ewPresales, ewPresalesAdmin)
xadmin.site.register(ewProject, ewProjectAdmin)
xadmin.site.register(ProjectResource, ProjectResourceAdmin)
# xadmin.site.register(ProjectBackup, ProjectBackupAdmin)
xadmin.site.register(ProjectPay, ProjectPayAdmin)
# xadmin.site.register(ProjectHrCost, ProjectHrCostAdmin)
# xadmin.site.register(ProjectCost, ProjectCostAdmin)
xadmin.site.register(ewProjectCheck, ewProjectCheckAdmin)
xadmin.site.register(ProjectReceived, ProjectReceivedAdmin)
xadmin.site.register(ProjectChange, ProjectChangeAdmin)


xadmin.site.register(ewReport, ewReportAdmin)
xadmin.site.register(ReportResource, ReportResourceAdmin)
xadmin.site.register(ReportUser, ReportUserAdmin)


