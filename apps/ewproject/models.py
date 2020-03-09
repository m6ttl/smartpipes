# encoding: utf-8

from datetime import datetime
import time
from django.db import models
from django.db.models import Sum,Count,Max,Min,Avg

from users.models import UserProfile

from DjangoUeditor.models import UEditorField

# Create your models here.

def get_kargs(**kwargs):
    return kwargs


# 字符串时间转换函数
def to_date(datetime1, format_date):
    Normaltime = datetime.datetime.strptime(datetime1, format_date)
    return Normaltime


# datetime时间转为字符串
def to_char(datetime1, format_ymd):
    str1 = datetime1.strftime(format_ymd)
    return str1


# datetime时间转为时间戳
def date_to_datetamp(dt1):
    Unixtime = time.mktime(time.strptime(dt1.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S'))
    return Unixtime


# 时间戳转为datetime时间
def datetamp_to_date(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt


# 多久之前 （传入时间戳）
def date_go(t):
    delta = int(time.time() - t)
    if delta < 60:
        return '刚才'
    if delta < 60 * 60:
        return '%s分钟前' % (delta // 60)
    if delta < 60 * 60 * 24:
        return '%s小时前' % (delta // (60 * 60))
    if delta < 60 * 60 * 24 * 31:
        return '%s天前' % (delta // (60 * 60 * 24))
    if delta < 60 * 60 * 24 * 365:
        return '%s月前' % (delta // (60 * 60 * 24 * 31))
    return '%s年前' % (delta // (60 * 60 * 24 * 365))

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

class ewProject(models.Model):
    ORG_CHOICES = (
        (u"营销",u"营销"),
        (u"生产",u"生产"),
        (u"城市服务",u"城市服务"),
        (u"智慧水务",u"智慧水务")
    )
    STATUS_CHOICES = (
        (u"在建", u"在建"),
        (u"已结案", u"已结案"),
        (u"结算", u"结算"),
        (u"取消", u"取消")
    )
    p_id = models.CharField(max_length=24, verbose_name=u"任务单编号")
    p_month = models.CharField(max_length=10, verbose_name=u"月份",default='2019/01')
    name = models.CharField(max_length=128, verbose_name=u"项目名称")

    province = models.CharField(max_length=20, verbose_name=u"省", null=True, blank=True)
    city = models.CharField(max_length=20, verbose_name=u"地名", null=True, blank=True)
    area_rank = models.CharField(max_length=20, verbose_name=u"级别",default='市',null=True, blank=True)

    bargain_m = models.IntegerField(default=0, verbose_name=u"合同金额", blank=True, null=True)
    task_hard_m = models.IntegerField(default=0, verbose_name=u"合同硬件金额", blank=True, null=True)
    task_soft_m = models.IntegerField(default=0, verbose_name=u"合同软件金额", blank=True, null=True)
    sales = models.CharField(max_length=20, verbose_name=u"销售人员", blank=True, null=True)
    dept = models.CharField(max_length=20, verbose_name=u"销售部门", blank=True, null=True)

    bargain_memo = UEditorField(verbose_name=u"合同内容描述", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    pay_memo = UEditorField(verbose_name=u"付款方式说明", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    schedule_memo = UEditorField(verbose_name=u"项目工期说明", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    p_schedule_memo = models.CharField(max_length=1024, verbose_name=u"合同工期要求", blank=True, null=True)

    task_m = models.IntegerField(default=0, verbose_name=u"任务单金额", blank=True, null=True)
    p_dept = models.CharField(max_length=40, verbose_name=u"所属部门", blank=True, null=True)
    p_pm  = models.CharField(max_length=30, verbose_name=u"项目经理", blank=True, null=True)
    builder_date = models.DateField(blank=True,verbose_name=u"立项日期", null=True)

    p_org = models.CharField(choices=ORG_CHOICES, max_length=40, verbose_name=u"大类", blank=True, null=True)
    p_type = models.CharField(max_length=40, verbose_name=u"分项", blank=True, null=True)
    p_kind = models.CharField(max_length=40, verbose_name=u"分类", blank=True, null=True)
    p_status = models.CharField(choices=STATUS_CHOICES, max_length=40, verbose_name=u"类型", blank=True, null=True)


#  工期
    p_plan_memo = UEditorField(verbose_name=u"里程碑信息", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    p_begin_date = models.DateField(verbose_name=u"计划开始日期", blank=True, null=True)
    p_s_use_date = models.DateField(verbose_name=u"计划完成日期", blank=True, null=True)
    p_s_chk_date = models.DateField(verbose_name=u"计划验收日期", blank=True, null=True)

    c_real_chk_date = models.DateField(verbose_name=u"结案时间", blank=True, null=True)
    c_delay_m = models.IntegerField(default=0, verbose_name = u"延期月份", blank=True, null=True)
    c_sched_s = models.IntegerField(default=0, verbose_name = u"工期评分", blank=True, null=True)

# 费用
    p_back_m = models.IntegerField(default=0, verbose_name=u"已回款金额", blank=True, null=True)
    p_back_scale = models.IntegerField(default=0, verbose_name=u"回款比例%", blank=True, null=True)

    p_pay = models.IntegerField(default=0, verbose_name = u"采购成本", blank=True, null=True)
    p_project = models.IntegerField(default=0, verbose_name = u"项目成本", blank=True, null=True)
    p_total = models.IntegerField(default=0, verbose_name = u"成本合计", blank=True, null=True)
    p_profit = models.IntegerField(default=0, verbose_name = u"盈利", blank=True, null=True)

    p_project_scale = models.IntegerField(default=0, verbose_name=u"已发生比例%", blank=True, null=True)

    c_m_project = models.IntegerField(default=0, verbose_name = u"当月项目成本", blank=True, null=True)
    c_m_pay = models.IntegerField(default=0, verbose_name = u"当月采购成本", blank=True, null=True)
    c_m_total = models.IntegerField(default=0, verbose_name = u"当月总成本", blank=True, null=True)

    p_budget_memo = UEditorField(verbose_name=u"预算概要", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    c_budget_m = models.IntegerField(default=0, verbose_name = u"预算", blank=True, null=True)
    c_final_m = models.IntegerField(default=0, verbose_name=u"决算", blank=True, null=True)
    c_diff_m = models.IntegerField(default=0, verbose_name=u"预决算盈亏", blank=True, null=True)

    c_cash_cost = models.IntegerField(default=0, verbose_name=u"资金成本", blank=True, null=True)
    c_cost_s = models.IntegerField(default=0, verbose_name = u"费用评分", blank=True, null=True)

# 文档
    c_filelist_memo = UEditorField(verbose_name=u"文档检视明细", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)
    c_file_memo = UEditorField(verbose_name=u"文件", width=600, height=100, imagePath="courses/ueditor/", filePath="courses/ueditor/",blank=True, null=True)

    c_week = models.IntegerField(default=0, verbose_name=u"项目有效周", blank=True, null=True)
    c_week_report = models.IntegerField(default=0, verbose_name=u"周报数", blank=True, null=True)
    c_week_s = models.IntegerField(default=0, verbose_name=u"周报评分", blank=True, null=True)

    c_filechklist_c = models.IntegerField(default=0, verbose_name=u"检视表", blank=True, null=True)
    c_filechklist_s = models.IntegerField(default=0, verbose_name=u"检视表评分", blank=True, null=True)

    c_ys_c = models.IntegerField(default=0, verbose_name=u"预算", blank=True, null=True)
    c_ys_s = models.IntegerField(default=0, verbose_name=u"预算评分", blank=True, null=True)

    c_jh_c = models.IntegerField(default=0, verbose_name=u"计划", blank=True, null=True)
    c_jh_s = models.IntegerField(default=0, verbose_name=u"计划评分", blank=True, null=True)

    c_js_c = models.IntegerField(default=0, verbose_name=u"决算", blank=True, null=True)
    c_js_s = models.IntegerField(default=0, verbose_name=u"决算评分", blank=True, null=True)

    c_ysb_c = models.IntegerField(default=0, verbose_name=u"验收报告", blank=True, null=True)
    c_ysb_s = models.IntegerField(default=0, verbose_name=u"验收报告评分", blank=True, null=True)

    c_jj_c = models.IntegerField(default=0, verbose_name=u"维护交接作业书", blank=True, null=True)
    c_jj_s = models.IntegerField(default=0, verbose_name=u"交接评分", blank=True, null=True)

    c_code_backup_c = models.IntegerField(default=0, verbose_name=u"源码备份", blank=True, null=True)
    c_code_backup_s = models.IntegerField(default=0, verbose_name=u"源码备份评分", blank=True, null=True)

    c_data_backup_c = models.IntegerField(default=0, verbose_name=u"数据库备份", blank=True, null=True)
    c_data_backup_s = models.IntegerField(default=0, verbose_name=u"数据库备份评分", blank=True, null=True)

    c_file_s = models.IntegerField(default=0, verbose_name=u"文档评分", blank=True, null=True)

# 总分
    c_total_s = models.IntegerField(default=0, verbose_name=u"总分", blank=True, null=True)
    c_date = models.DateField(verbose_name=u"评分日期", blank=True, null=True)


    class Meta:
        verbose_name = u"项目监管"
        verbose_name_plural = verbose_name

    def get_rec_sum(self):
        return self.projectreceived_set.aggregate(s1=Sum('pay')).get('s1')
    get_rec_sum.short_description = '回款'

    def get_rec_pst(self):
        return self.get_rec_sum
    # return int(self.p_back_m) / int(self.p_money) * 100
    get_rec_pst.short_description = '回款比例'

    def __str__(self):
        return self.name

# 项目资源
class ProjectResource(models.Model):
    # 因为一个项目对应很多资源。所以在项目资源表中将项目设置为外键。
    # 作为一个字段来让我们可以知道这个资源对应那个项目
    project = models.ForeignKey(ewProject, on_delete=models.CASCADE, verbose_name=u"项目")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"项目资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》项目的资源: {1}'.format(self.project,self.name)

# 项目变更日志
class ProjectChange(models.Model):
    project = models.ForeignKey(ewProject, on_delete=models.CASCADE, verbose_name=u"项目")
    name = models.CharField(max_length=100, verbose_name=u"变更内容")
    kind = models.CharField(max_length=40, verbose_name=u"类型", blank=True, null=True)
    old = models.CharField(max_length=40, verbose_name=u"原值", blank=True, null=True)
    new = models.CharField(max_length=40, verbose_name=u"现值", blank=True, null=True)
    c_date = models.DateField(default=datetime.now, verbose_name=u"变更时间", blank=True, null=False)

    class Meta:
        verbose_name = u"项目重要变更"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》项目的重要变更: {1}'.format(self.project, self.name)


# 项目回款记录
class ProjectReceived(models.Model):
    REC_CHOICES = (
        (u"首付款", u"首付款"),
        (u"启动款", u"启动款"),
        (u"上线款", u"上线款"),
        (u"验收款", u"验收款"),
        (u"质保款", u"质保款")
    )
    project = models.ForeignKey(ewProject, on_delete=models.CASCADE, verbose_name=u"项目")
    p_month = models.CharField(max_length=20, verbose_name=u"月份", null=False, default = '2019/01')
    kind = models.CharField(choices=REC_CHOICES, max_length=40, verbose_name=u"类型", blank=True, null=True)
    builder = models.CharField(max_length=10, verbose_name=u"登记人", blank=True, null=True)
    build_date = models.DateField(verbose_name=u"发生日期", default=datetime.now, blank=True, null=True)
    pay = models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=False, verbose_name='金额')

    class Meta:
        verbose_name = u"项目回款"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》项目的项目回款: {1}'.format(self.project, self.kind)


#项目采购记录
class ProjectPay(models.Model):
    project = models.ForeignKey(ewProject, on_delete=models.CASCADE, verbose_name=u"项目")
    builder = models.CharField(max_length=10, verbose_name=u"经办人", blank=True, null=True)
    build_date = models.DateField(verbose_name=u"日期", default=datetime.now, blank=True, null=True)
    pay_id = models.CharField(max_length=40, verbose_name=u"申请单号", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    script = models.CharField(max_length=100, verbose_name=u"型号")
    kind = models.CharField(max_length=100, verbose_name=u"付款描述", blank=True, null=True)
    dept = models.CharField(max_length=40, verbose_name=u"部门", blank=True, null=True)
    vendor = models.CharField(max_length=100, verbose_name=u"供应商")
    qty =  models.IntegerField(default=0, verbose_name = u"数量", blank=True, null=True)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='单价'),
    pay = models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=False, verbose_name='总金额')

    class Meta:
        verbose_name = u"项目采购"
        verbose_name_plural = verbose_name


    def __str__(self):
        return '《{0}》项目的采购: {1}'.format(self.project, self.name)

#验收信息
class ewProjectCheck(ewProject):
    class Meta:
        verbose_name = u"验收信息"
        verbose_name_plural = verbose_name
        proxy = True #必须这么些不会要求 migrite

# # from django.db import models
# class JupyterFileField(models.FileField):
#     def pre_save(self, model_instance, add):
#         file = super().pre_save(model_instance, add)
#         if file and not file._committed:
#             # Commit the file to storage prior to saving the model
#             file.name = 'XX' + file.name
#             file.save(file.name, file.file, save=False)
#         return file


class JupyterFileField(models.FileField):
    # __metaclass__ = models.SubfieldBase
    # description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(FileField, self).__init__(*args, **kwargs)

    #业务报告
class ewReport(models.Model):
    RPT_CHOICES = (
        (u"项目监管周报", u"项目监管周报"),
        (u"项目监管月度分析", u"项目监管月度分析"),
        (u"行业情况通报", u"行业情况通报"),
        (u"分析报告", u"分析报告")
    )
    name = models.CharField(max_length=100, verbose_name=u"名称")
    typen = models.CharField(max_length=30, choices=RPT_CHOICES, verbose_name=u"报告类型", blank=True, null=True)
    builder = models.CharField(max_length=10, verbose_name=u"创建人", blank=True, null=True)
    build_date = models.DateTimeField(verbose_name=u"上传时间", default=datetime.now, blank=True, null=True)
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"HTML报告",
        max_length=100)

    # download = models.JupyterFileField(
    #     upload_to="course/resource/%Y/%m",
    #     verbose_name=u"HTML报告",
    #     max_length=100)

    def get_day_go(self):
        # 获取课程交流数的方法
        return date_go(date_to_datetamp(self.build_date))
    get_day_go.short_description = '发布时间'

    # 获取学习这门报告的用户
    # 替代标签:course.usercourse_set.get_queryset|slice:":1"
    def get_learn_users(self):
    #     # 谁的里面添加了它做外键，他都可以取出来
        return self.reportuser_set.all()[:5]

    class Meta:
        verbose_name = u"分析报告"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

# 报告附件
class ReportResource(models.Model):
    # 因为一个项目对应很多资源。所以在项目资源表中将项目设置为外键。
    # 作为一个字段来让我们可以知道这个资源对应那个项目
    project = models.ForeignKey(ewReport, on_delete=models.CASCADE, verbose_name=u"报告")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    # 这里定义成文件类型的field，后台管理系统中会直接有上传的按钮。
    # FileField也是一个字符串类型，要指定最大长度。
    download = models.FileField(
        upload_to="course/resource/%Y/%m",
        verbose_name=u"资源文件",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"报告附件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '《{0}》报告的资源: {1}'.format(self.project,self.name)

# 用户报告阅读表
class ReportUser(models.Model):
    # 会涉及两个外键: 1. 用户， 2. 报告。import进来
    report = models.ForeignKey(ewReport, on_delete=models.CASCADE, verbose_name=u"报告")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"阅读时间")

    class Meta:
        verbose_name = u"报告阅读用用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})阅读了{1} '.format(self.user, self.report)