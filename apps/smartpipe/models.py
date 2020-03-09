# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField

from django.contrib.auth.models import User

from users.models import UserProfile

class smartpipe(models.Model):
    ### 1、基本属性
    name = models.CharField(max_length=60, verbose_name=u"名称", blank=True, null=True)
    caliber = models.CharField(max_length=10, verbose_name=u"口径", blank=True, null=True)
    sn = models.CharField(max_length=40, verbose_name=u"编号", blank=True, null=True)
    label = models.CharField(max_length=60, verbose_name=u"电子标签", blank=True, null=True)
    vendor_id = models.CharField(max_length=20, verbose_name=u"供应商", blank=True, null=True)

    ### 2、MQTT属性
    profile_name = models.CharField(max_length=50, verbose_name=u"消息名称", blank=True, null=True)
    profile_type = models.CharField(max_length=50, verbose_name=u"消息类型", blank=True, null=True)
    broker_address = models.CharField(max_length=50, verbose_name=u"消息ip", blank=True, null=True)
    broker_port = models.IntegerField(default=0, verbose_name=u"端口", blank=True, null=True)
    client_id = models.CharField(max_length=50, verbose_name=u"客户端ID", blank=True, null=True)
    conn_timeout = models.IntegerField(default=0, verbose_name=u"连接timeout", blank=True, null=True)
    MQTT_version = models.CharField(max_length=40, verbose_name=u"MQTT版本", blank=True, null=True)
    profile_version = models.CharField(max_length=40, verbose_name=u"协议版本", blank=True, null=True)
    publish_item = models.CharField(max_length=100, verbose_name=u"发布信息项", blank=True, null=True)
    msg_sec = models.IntegerField(default=0, verbose_name=u"发布时间间隔", blank=True, null=True)
    collection_min = models.IntegerField(default=0, verbose_name=u"采集时间间隔", blank=True, null=True)

    ### 3、物流信息
    po_date = models.DateTimeField(default=datetime.now, verbose_name=u"订单时间", blank=True, null=True)
    check_date = models.DateTimeField(default=datetime.now, verbose_name=u"检验时间", blank=True, null=True)
    check_file = models.CharField(max_length=100, verbose_name=u"检验报告", blank=True, null=True)
    check_spec = UEditorField(verbose_name=u"标定数据", width=600, height=300, imagePath="courses/ueditor/",
                              filePath="courses/ueditor/", default='', blank=True, null=True)
    factory_date = models.DateTimeField(default=datetime.now, verbose_name=u"出厂时间", blank=True, null=True)
    arrival_date = models.DateTimeField(default=datetime.now, verbose_name=u"到货时间", blank=True, null=True)

    ### 4、安装信息
    # owner_id = models.CharField(max_length=20, verbose_name=u"业主编号", blank=True, null=True)
    project_id = models.CharField(max_length=20, verbose_name=u"项目编号", blank=True, null=True)
    # RTU_id = models.CharField(max_length=50, verbose_name=u"RTU编号", blank=True, null=True)
    depth = models.IntegerField(default=0, verbose_name=u"埋深", blank=True, null=True)
    install_date = models.DateTimeField(default=datetime.now, verbose_name=u"安装时间", blank=True, null=True)
    interface = models.CharField(max_length=30, verbose_name=u"接口方式", blank=True, null=True)
    pipeline = models.CharField(max_length=30, verbose_name=u"管道材质", blank=True, null=True)
    longitude = models.FloatField(verbose_name=u"安装经度", blank=True, null=True)
    latitude = models.FloatField(verbose_name=u"安装纬度", blank=True, null=True)
    # cancel_flag = models.IntegerField(default=0, verbose_name=u"是否报废", blank=True, null=True)

    ### 5、阈值信息
    pressure_low = models.FloatField(verbose_name=u"压力报警低限", blank=True, null=True)
    pressure_high = models.FloatField(verbose_name=u"压力告警高限", blank=True, null=True)
    power_low = models.FloatField(verbose_name=u"电力告警低限", blank=True, null=True)
    flow_l = models.CharField(max_length=128, verbose_name=u"分析告警", blank=True, null=True)

    class Meta:
        verbose_name = u"智慧管件"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


# pipe_id = models.ForeignKey(smartpipe, on_delete=models.SET_NULL, verbose_name=u"管件编号", null=True)
class pipedetail(models.Model):
    ### 7、管件使用明细
    name = models.CharField(max_length=30, verbose_name=u"消息名称", blank=True, null=True)
    pipe_id = models.ForeignKey(smartpipe, on_delete=models.CASCADE, verbose_name=u"管件编号")
    collection_time = models.DateTimeField(default=datetime.now, verbose_name=u"采集时间", blank=True, null=True)
    tem = models.FloatField(verbose_name=u"温度", blank=True, null=True)
    pressure = models.FloatField(verbose_name=u"压力", blank=True, null=True)
    ins_flow = models.FloatField(verbose_name=u"瞬间流量", blank=True, null=True)
    tot_flow = models.FloatField(verbose_name=u"累计流量", blank=True, null=True)
    power = models.FloatField(verbose_name=u"电力情况", blank=True, null=True)

    class Meta:
        verbose_name = u"管件使用明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class workorder(models.Model):
    ### 8、管件运维工单明细
    pipe_id = models.ForeignKey(smartpipe, on_delete=models.SET_NULL, verbose_name=u"管件编号", blank=True, null=True)
    name = models.CharField(max_length=500, verbose_name=u"名称", blank=True, null=True)
    alert_id = models.CharField(max_length=40, verbose_name=u"关联告警事务                         ", blank=True, null=True)
    order_p = models.CharField(max_length=40, verbose_name=u"安排人员", blank=True, null=True)
    turnup_date = models.DateTimeField(default=datetime.now, verbose_name=u"到场时间", blank=True, null=True)
    turnup_lon = models.CharField(max_length=40, verbose_name=u"到场打卡经度", blank=True, null=True)
    turnup_lat = models.CharField(max_length=40, verbose_name=u"到场打卡纬度", blank=True, null=True)
    accident_hand = models.CharField(max_length=500, verbose_name=u"工单处理情况描述", blank=True, null=True)
    accident_pic = models.CharField(max_length=200, verbose_name=u"工单处理图片上传", blank=True, null=True)
    accident_date = models.DateTimeField(default=datetime.now, verbose_name=u"处理完成时间", blank=True, null=True)
    accident_result = models.CharField(max_length=50, verbose_name=u"处理结果（已完成、取消、未完成）", blank=True, null=True)
    accident_star = models.CharField(max_length=50, verbose_name=u"处理评级（1星—5星）", blank=True, null=True)
    class Meta:
        verbose_name = u"管件运维工单明细"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class alert(models.Model):
    ### 9、自动告警
    name = models.CharField(max_length=50, verbose_name=u"告警类型", blank=True, null=True)
    pipe_id = models.ForeignKey(smartpipe, on_delete=models.CASCADE, verbose_name=u"管件编号")
    reason = models.CharField(max_length=500, verbose_name=u"告警依据", blank=True, null=True)
    alert_date = models.DateTimeField(default=datetime.now, verbose_name=u"告警时间", blank=True, null=True)
    alert_hand = UEditorField(verbose_name=u"详细描述", width=600, height=300, imagePath="courses/ueditor/",
                              filePath="courses/ueditor/", default='', blank=True, null=True)
    alert_result = models.CharField(max_length=50, verbose_name=u"告警解决情况（已完成、取消、未完成）", blank=True, null=True)
    class Meta:
        verbose_name = u"自动告警"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



# class owner(models.Model):
#     ### 11、业主信息
#     owner_id = models.CharField(max_length=40, verbose_name=u"编号", blank=True, null=True)
#     name = models.CharField(max_length=100, verbose_name=u"名称", blank=True, null=True)
#     info = models.CharField(max_length=500, verbose_name=u"业主信息", blank=True, null=True)
#     concact = models.CharField(max_length=100, verbose_name=u"联系人", blank=True, null=True)
#     phone_no = models.CharField(max_length=50, verbose_name=u"手机", blank=True, null=True)
#     wx = models.CharField(max_length=100, verbose_name=u"微信名", blank=True, null=True)
#     email = models.CharField(max_length=100, verbose_name=u"email", blank=True, null=True)
#     reg_date = models.DateTimeField(default=datetime.now, verbose_name=u"注册时间", blank=True, null=True)
#     address = models.CharField(max_length=300, verbose_name=u"地址", blank=True, null=True)
#     longitude = models.CharField(max_length=40, verbose_name=u"经度", blank=True, null=True)
#     latitude = models.CharField(max_length=40, verbose_name=u"纬度", blank=True, null=True)
#     class Meta:
#         verbose_name = u"业主信息"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name

class project(models.Model):
    ### 12、项目
    project_id = models.CharField(max_length=40, verbose_name=u"编号", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name=u"名称", blank=True, null=True)
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, verbose_name=u"用户", default='', blank=True, null=True)
    # owner_id = models.ForeignKey(owner, on_delete=models.SET_NULL, verbose_name=u"业主"，blank=True, null=True)
    info = UEditorField(verbose_name=u"项目信息", width=600, height=300, imagePath="courses/ueditor/",
                        filePath="courses/ueditor/", default='', blank=True, null=True)
    contract = models.CharField(max_length=100, verbose_name=u"联系人", blank=True, null=True)
    phone_no = models.CharField(max_length=50, verbose_name=u"手机", blank=True, null=True)
    wx = models.CharField(max_length=100, verbose_name=u"微信名", blank=True, null=True)
    email = models.CharField(max_length=100, verbose_name=u"email", blank=True, null=True)
    reg_date = models.DateTimeField(default=datetime.now, verbose_name=u"注册时间", blank=True, null=True)
    address = models.CharField(max_length=300, verbose_name=u"地址", blank=True, null=True)
    longitude = models.CharField(max_length=40, verbose_name=u"经度", blank=True, null=True)
    latitude = models.CharField(max_length=40, verbose_name=u"纬度", blank=True, null=True)

    class Meta:
        verbose_name = u"项目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class vendor(models.Model):
    ### 13、供应商
    vendor_id = models.CharField(max_length=40, verbose_name=u"编号", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name=u"名称", blank=True, null=True)
    info = UEditorField(verbose_name=u"供应商信息", width=600, height=300, imagePath="courses/ueditor/",
                        filePath="courses/ueditor/", default='', blank=True, null=True)
    contract = models.CharField(max_length=100, verbose_name=u"联系人", blank=True, null=True)
    phone_no = models.CharField(max_length=50, verbose_name=u"手机", blank=True, null=True)
    wx = models.CharField(max_length=100, verbose_name=u"微信名", blank=True, null=True)
    email = models.CharField(max_length=100, verbose_name=u"email", blank=True, null=True)
    reg_date = models.DateTimeField(default=datetime.now, verbose_name=u"注册时间", blank=True, null=True)
    address = models.CharField(max_length=300, verbose_name=u"地址", blank=True, null=True)
    longitude = models.CharField(max_length=40, verbose_name=u"经度", blank=True, null=True)
    latitude = models.CharField(max_length=40, verbose_name=u"纬度", blank=True, null=True)
    class Meta:
        verbose_name = u"供应商"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class design(models.Model):
    ### 14、设计院
    design_id = models.CharField(max_length=40, verbose_name=u"编号", blank=True, null=True)
    name = models.CharField(max_length=100, verbose_name=u"名称", blank=True, null=True)
    info = UEditorField(verbose_name=u"设计院信息", width=600, height=300, imagePath="courses/ueditor/",
                        filePath="courses/ueditor/", default='', blank=True, null=True)
    contract = models.CharField(max_length=100, verbose_name=u"联系人", blank=True, null=True)
    phone_no = models.CharField(max_length=50, verbose_name=u"手机", blank=True, null=True)
    wx = models.CharField(max_length=100, verbose_name=u"微信名", blank=True, null=True)
    email = models.CharField(max_length=100, verbose_name=u"email", blank=True, null=True)
    reg_date = models.DateTimeField(default=datetime.now, verbose_name=u"注册时间", blank=True, null=True)
    address = models.CharField(max_length=300, verbose_name=u"地址", blank=True, null=True)
    longitude = models.CharField(max_length=40, verbose_name=u"经度", blank=True, null=True)
    latitude = models.CharField(max_length=40, verbose_name=u"纬度", blank=True, null=True)
    class Meta:
        verbose_name = u"设计院"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    # class porder(models.Model):
    #     ### 10、订单信息
    #     project_id = models.ForeignKey(project, on_delete=models.SET_NULL, verbose_name=u"项目", blank=True, null=True)
    #     name = models.CharField(max_length=100, verbose_name=u"名称", blank=True, null=True)
    #     info = models.CharField(max_length=500, verbose_name=u"业主信息", blank=True, null=True)
    #     concact = models.CharField(max_length=100, verbose_name=u"联系人", blank=True, null=True)
    #     phone_no = models.CharField(max_length=50, verbose_name=u"手机", blank=True, null=True)
    #     wx = models.CharField(max_length=100, verbose_name=u"微信名", blank=True, null=True)
    #     email = models.CharField(max_length=100, verbose_name=u"email", blank=True, null=True)
    #     po_info = models.CharField(max_length=500, verbose_name=u"订单描述", blank=True, null=True)
    #
    #     class Meta:
    #         verbose_name = u"订单信息"
    #         verbose_name_plural = verbose_name
    #
    #     def __str__(self):
    #         return self.name