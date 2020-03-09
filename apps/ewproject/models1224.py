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


# # 项目监管
# class ewProject(models.Model):
#     p_id = models.CharField(max_length=24, verbose_name=u"任务单编号")
#     p_month = models.CharField(max_length=10, verbose_name=u"月份",default='2019/01')
#     name = models.CharField(max_length=128, verbose_name=u"项目名称")
#
#     province = models.CharField(max_length=20, verbose_name=u"省", null=True, blank=True)
#     city = models.CharField(max_length=20, verbose_name=u"地名", null=True, blank=True)
#
#     area_rank = models.CharField(max_length=20, verbose_name=u"级别",default='市')
#     bargain_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"合同总金额", blank=True, null=True)
#     task_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"软件任务单金额", blank=True, null=True)
#     sales = models.CharField(max_length=20, verbose_name=u"销售人员", blank=True, null=True)
#     builder_date = models.DateTimeField(blank=True,verbose_name=u"创建日期", null=True)
#     modi_man = models.CharField(max_length=20, verbose_name=u"修改人", blank=True, null=True)
#     cust_name = models.CharField(max_length=128, verbose_name=u"客户名称", blank=True, null=True)
#     owner = models.CharField(max_length=20, verbose_name=u"所有人", blank=True, null=True)
#     dept = models.CharField(max_length=20, verbose_name=u"所属部门", blank=True, null=True)
#     modi_date = models.DateTimeField(blank=True, verbose_name=u"修改日期", null=True)
#     task_hard_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"合同硬件金额", blank=True, null=True)
#     task_soft_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"合同硬件金额", blank=True, null=True)
#     bargain_memo = UEditorField(verbose_name=u"合同内容描述", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
#     pay_memo = UEditorField(verbose_name=u"付款方式说明", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
#     schedule_memo = UEditorField(verbose_name=u"项目工期说明", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
#     contract = models.CharField(max_length=20, verbose_name=u"客户联系人", blank=True, null=True)
#     contract_phone = models.CharField(max_length=30, verbose_name=u"客户联系人手机", blank=True, null=True)
#     other_memo = models.CharField(max_length=1024, verbose_name=u"重要情况说明", blank=True, null=True)
#     bargain_id = models.CharField(max_length=30,verbose_name=u"系统合同编号", blank=True, null=True)
#     contract_title = models.CharField(max_length=30, verbose_name=u"客户联系人职务", blank=True, null=True)
#     contract_address = models.CharField(max_length=30, verbose_name=u"客户联系人地址", blank=True, null=True)
#
#     p_dept = models.CharField(max_length=40, verbose_name=u"所属部门", blank=True, null=True)
#     p_org = models.CharField(max_length=40, verbose_name=u"大类", blank=True, null=True)
#     p_type = models.CharField(max_length=40, verbose_name=u"分项", blank=True, null=True)
#     p_kind = models.CharField(max_length=40, verbose_name=u"分类", blank=True, null=True)
#     p_money = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"合同金额", blank=True, null=True)
#     p_back_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"已回款金额", blank=True, null=True)
#     p_back_scale = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"回款比例", blank=True, null=True)
#     p_m1 = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"首付款", blank=True, null=True)
#     p_m2 = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"启动款", blank=True, null=True)
#     p_m3 = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"上线款", blank=True, null=True)
#     p_m4 = models.DecimalField(max_digits=12, decimal_places=0, verbose_name = u"验收款", blank=True, null=True)
#     p_m5 = models.DecimalField(max_digits=12, decimal_places=0, verbose_name = u"质保款", blank=True, null=True)
#     p_task_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name = u"软件实施费", blank=True, null=True)
#     p_project_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name = u"人工差旅费", blank=True, null=True)
#     p_project_scale = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"已发生费比例", blank=True, null=True)
#
#     p_schedule_memo = models.CharField(max_length=1024, verbose_name=u"合同工期要求", blank=True, null=True)
#     p_s_use_date = models.DateTimeField(verbose_name=u"要求上线日期", blank=True, null=True)
#     p_s_chk_date = models.DateTimeField(verbose_name=u"要求验收日期", blank=True, null=True)
#     p_pm  = models.CharField(max_length=30, verbose_name=u"项目经理", blank=True, null=True)
#
#     p_do  = models.CharField(max_length=30, verbose_name=u"财务进度", blank=True, null=True)
#
#     c_chk_date = models.DateTimeField(verbose_name=u"内部验收日期", blank=True, null=True)
#     c_chk_man = models.CharField(max_length=200, verbose_name=u"验收参与人员", blank=True, null=True)
#
#     c_budget_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name = u"预算", blank=True, null=True)
#     c_final_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"决算", blank=True, null=True)
#     c_diff_m = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"预决算盈亏", blank=True, null=True)
#
#     c_cash_cost = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"资金成本", blank=True, null=True)
#     c_pay_cost = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"采购成本", blank=True, null=True)
#
#     c_use_date = models.DateTimeField(verbose_name=u"实际上线日期", blank=True, null=True)
#     c_chk_date = models.DateTimeField(verbose_name=u"实际验收日期", blank=True, null=True)
#
#     c_code_backup_date = models.DateTimeField(verbose_name=u"代码备份时间", blank=True, null=True)
#     c_database_backup_date = models.DateTimeField( verbose_name=u"数据库备份时间", blank=True, null=True)
#
#     c_week = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"项目有效周", blank=True, null=True)
#     c_week_report = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"周报数", blank=True, null=True)
#
#     c_filechklist_c = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"检视表要求文档数", blank=True, null=True)
#     c_file_audit_c = models.DecimalField(max_digits=12, decimal_places=0, verbose_name=u"检视表要求文档数", blank=True, null=True)
#     c_file_memo = UEditorField(verbose_name=u"文档检视明细", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
#
#     class Meta:
#         verbose_name = u"项目监管"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name



# 项目监管
class ewProject(models.Model):
    ORG_CHOICES = (
        (u"营销",u"营销"),
        (u"生产",u"生产"),
        (u"城市服务",u"城市服务"),
        (u"智慧水务",u"智慧水务")
    )
    STATUS_CHOICES = (
        (u"已启动",u"已启动"),
        (u"已验收",u"已验收"),
        (u"取消",u"取消")
    )
    p_id = models.CharField(max_length=24, verbose_name=u"任务单编号")
    p_month = models.CharField(max_length=10, verbose_name=u"月份",default='2019/01')
    name = models.CharField(max_length=128, verbose_name=u"项目名称")

    province = models.CharField(max_length=20, verbose_name=u"省", null=True, blank=True)
    city = models.CharField(max_length=20, verbose_name=u"地名", null=True, blank=True)

    area_rank = models.CharField(max_length=20, verbose_name=u"级别",default='市',null=True, blank=True)
    bargain_m = models.IntegerField(default=0, verbose_name=u"合同总金额", blank=True, null=True)
    task_m = models.IntegerField(default=0, verbose_name=u"软件任务单金额", blank=True, null=True)
    sales = models.CharField(max_length=20, verbose_name=u"销售人员", blank=True, null=True)
    builder_date = models.DateField(blank=True,verbose_name=u"创建日期", null=True)
    modi_man = models.CharField(max_length=20, verbose_name=u"修改人", blank=True, null=True)
    cust_name = models.CharField(max_length=128, verbose_name=u"客户名称", blank=True, null=True)
    owner = models.CharField(max_length=20, verbose_name=u"所有人", blank=True, null=True)
    dept = models.CharField(max_length=20, verbose_name=u"所属部门", blank=True, null=True)
    modi_date = models.DateField(blank=True, verbose_name=u"修改日期", null=True)
    task_hard_m = models.IntegerField(default=0, verbose_name=u"合同硬件金额", blank=True, null=True)
    task_soft_m = models.IntegerField(default=0, verbose_name=u"合同软件金额", blank=True, null=True)
    bargain_memo = UEditorField(verbose_name=u"合同内容描述", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    pay_memo = UEditorField(verbose_name=u"付款方式说明", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    schedule_memo = UEditorField(verbose_name=u"项目工期说明", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    contract = models.CharField(max_length=20, verbose_name=u"客户联系人", blank=True, null=True)
    contract_phone = models.CharField(max_length=30, verbose_name=u"客户联系人手机", blank=True, null=True)
    other_memo = models.CharField(max_length=1024, verbose_name=u"重要情况说明", blank=True, null=True)
    bargain_id = models.CharField(max_length=30,verbose_name=u"系统合同编号", blank=True, null=True)
    contract_title = models.CharField(max_length=30, verbose_name=u"客户联系人职务", blank=True, null=True)
    contract_address = models.CharField(max_length=30, verbose_name=u"客户联系人地址", blank=True, null=True)

    p_dept = models.CharField(max_length=40, verbose_name=u"所属部门", blank=True, null=True)
    p_org = models.CharField(choices=ORG_CHOICES, max_length=40, verbose_name=u"大类", blank=True, null=True)
    p_type = models.CharField(max_length=40, verbose_name=u"分项", blank=True, null=True)
    p_kind = models.CharField(max_length=40, verbose_name=u"分类", blank=True, null=True)
    p_status = models.CharField(choices=STATUS_CHOICES, max_length=40, verbose_name=u"状态", blank=True, null=True)

    p_money = models.IntegerField(default=0, verbose_name=u"合同金额", blank=True, null=True)
    p_back_m = models.IntegerField(default=0, verbose_name=u"已回款金额", blank=True, null=True)
    p_back_scale = models.IntegerField(default=0, verbose_name=u"回款比例", blank=True, null=True)
    p_m1 = models.IntegerField(default=0, verbose_name=u"首付款", blank=True, null=True)
    p_m2 = models.IntegerField(default=0, verbose_name=u"启动款", blank=True, null=True)
    p_m3 = models.IntegerField(default=0, verbose_name=u"上线款", blank=True, null=True)
    p_m4 = models.IntegerField(default=0, verbose_name = u"验收款", blank=True, null=True)
    p_m5 = models.IntegerField(default=0, verbose_name = u"质保款", blank=True, null=True)
    p_task_m = models.IntegerField(default=0, verbose_name = u"软件实施费", blank=True, null=True)
    p_project_m = models.IntegerField(default=0, verbose_name = u"人工差旅费", blank=True, null=True)
    p_project_scale = models.IntegerField(default=0, verbose_name=u"已发生费比例", blank=True, null=True)

    p_schedule_memo = models.CharField(max_length=1024, verbose_name=u"合同工期要求", blank=True, null=True)
    p_s_use_date = models.DateField(verbose_name=u"要求上线日期", blank=True, null=True)
    p_s_chk_date = models.DateField(verbose_name=u"要求验收日期", blank=True, null=True)
    p_pm  = models.CharField(max_length=30, verbose_name=u"项目经理", blank=True, null=True)

    p_do  = models.CharField(max_length=30, verbose_name=u"财务进度", blank=True, null=True)

    c_chk_date = models.DateField(verbose_name=u"内部验收日期", blank=True, null=True)
    c_chk_man = models.CharField(max_length=200, verbose_name=u"验收参与人员", blank=True, null=True)

    c_budget_m = models.IntegerField(default=0, verbose_name = u"预算", blank=True, null=True)
    c_final_m = models.IntegerField(default=0, verbose_name=u"决算", blank=True, null=True)
    c_diff_m = models.IntegerField(default=0, verbose_name=u"预决算盈亏", blank=True, null=True)

    c_cash_cost = models.IntegerField(default=0, verbose_name=u"资金成本", blank=True, null=True)
    c_pay_cost = models.IntegerField(default=0, verbose_name=u"采购成本", blank=True, null=True)

    c_use_date = models.DateField(verbose_name=u"实际上线日期", blank=True, null=True)
    c_chk_date = models.DateField(verbose_name=u"实际验收日期", blank=True, null=True)

    c_code_backup_date = models.DateField(verbose_name=u"代码备份时间", blank=True, null=True)
    c_database_backup_date = models.DateField( verbose_name=u"数据库备份时间", blank=True, null=True)

    c_week = models.IntegerField(default=0, verbose_name=u"项目有效周", blank=True, null=True)
    c_week_report = models.IntegerField(default=0, verbose_name=u"周报数", blank=True, null=True)

    c_filechklist_c = models.IntegerField(default=0, verbose_name=u"检视表要求文档数", blank=True, null=True)
    c_file_audit_c = models.IntegerField(default=0, verbose_name=u"实际文档数", blank=True, null=True)
    c_file_memo = UEditorField(verbose_name=u"文档检视明细", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)

    class Meta:
        verbose_name = u"项目监管"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#源码备份信息
class ewProjectBackup(ewProject):
    class Meta:
        verbose_name = u"源码备份信息"
        verbose_name_plural = verbose_name
        proxy = True #必须这么些不会要求 migrite

#验收信息
class ewProjectCheck(ewProject):
    class Meta:
        verbose_name = u"验收信息"
        verbose_name_plural = verbose_name
        proxy = True #必须这么些不会要求 migrite


class ewReport(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"名称")
    typen = models.CharField(max_length=20, verbose_name=u"业务类型", blank=True, null=True)
    builder = models.CharField(max_length=10, verbose_name=u"创建人", blank=True, null=True)
    build_date = models.DateTimeField(verbose_name=u"上传时间", blank=True, null=True)
    title = models.CharField(max_length=128, verbose_name=u"标题", blank=True, null=True)
    detail = models.CharField(max_length=128, verbose_name=u"内容", blank=True, null=True)


    class Meta:
        verbose_name = u"分析报告"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name