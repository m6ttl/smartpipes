# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/9 0009 20:10'

from .models import smartpipe,pipedetail,workorder,alert,project,vendor,design


import xadmin
from xadmin.layout import Fieldset, Main, Side, Row

# ewPresales的admin管理器


class smartpipeAdmin(object):
    list_display = [
        'caliber',
        'name',
        'sn',
        'label',
        'vendor_id']
    search_fields = [
        'caliber',
        'sn',
        'label',
        'vendor_id']
    list_filter = [
        'caliber',
        'sn',
        'label',
        'vendor_id']
    model_icon = 'fa fa-map'
    form_layout = (
        Main(
            Fieldset('1、基本属性',
                     'name', Row('caliber', 'sn'), Row('label', 'vendor_id')),
            Fieldset('4、安装信息',
                     'project_id', 'depth', 'install_date', 'interface', 'pipeline', 'longitude', 'latitude'),
        )
        # Side(
        #     Fieldset('其它',
        #              'buy_date', 'expire_date', 'note', 'attachment', 'date'),
        # )
    )

    # def get_form_layout(self):
    #     self.form_layout = (
    #         Main(
    #             Fieldset('1、基本属性',
    #                      'name','caliber','sn','label','vendor_id'),
    #             Fieldset('4、安装信息',
    #                      'project_id', 'depth', 'install_date', 'interface', 'pipeline','longitude','latitude'),
    #         )
    #         # Side(
    #         #     Fieldset('其它',
    #         #              'buy_date', 'expire_date', 'note', 'attachment', 'date'),
    #         # )
    #     )
    #     return super(BasicAdmin, self).get_form_layout()

class pipedetailAdmin(object):
    list_display = [
        'name',
        'pipe_id',
        'collection_time',
        'pressure',
        'ins_flow',
        "tot_flow",
        "power"]
    search_fields = [
        'name',
        'pipe_id',
        'pressure',
        'ins_flow',
        "tot_flow",
        "power"]
    list_filter = [
        'name',
        'pipe_id',
        'pressure',
        'ins_flow',
        "tot_flow",
        "power"]
    model_icon = 'fa fa-info'


class workorderAdmin(object):
    list_display = [
        'pipe_id',
        'name',
        'alert_id',
        'order_p',
        'turnup_date',
        "turnup_lon",
        "turnup_lat",
        "accident_hand",
        "accident_pic",
        'accident_date',
        "accident_result",
        "accident_star"]
    search_fields = [
        'pipe_id',
        'name',
        'alert_id',
        'order_p',
        "turnup_lon",
        "turnup_lat",
        "accident_hand",
        "accident_pic",
        "accident_result",
        "accident_star"]
    list_filter = [
        'pipe_id',
        'name',
        'alert_id',
        'order_p',
        "turnup_lon",
        "turnup_lat",
        "accident_hand",
        "accident_pic",
        "accident_result",
        "accident_star"]
    model_icon = 'fa fa-address-card'


class alertAdmin(object):
    list_display = [
        'name',
        'pipe_id',
        'reason',
        'alert_date',
        "alert_hand",
        "alert_result"]
    search_fields = [
        'name',
        'pipe_id',
        'reason',
        "alert_hand",
        "alert_result"]
    list_filter = [
        'name',
        'pipe_id',
        'reason',
        "alert_hand",
        "alert_result"]
    model_icon = 'fa fa-bell-slash'


class poAdmin(object):
    list_display = [
        'owner_id',
        'name',
        'info',
        'concact',
        "phone_no",
        "wx",
        "email",
        "po_info"]
    search_fields = [
        'owner_id',
        'name',
        'info',
        'concact',
        "phone_no",
        "wx",
        "email"]
    list_filter = [
        'owner_id',
        'name',
        'info',
        'concact',
        "phone_no",
        "wx",
        "email"]
    model_icon = 'fa fa-address-card'

class ownerAdmin(object):
    list_display = [
        'owner_id',
        'name',
        'info',
        'concact',
        "phone_no",
        "wx",
        "email",
        "reg_date",
        "address",
        "longitude",
        "latitude"]
    search_fields = [
        'owner_id',
        'name',
        'info',
        'concact',
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    list_filter = [
        'owner_id',
        'name',
        'info',
        'concact',
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    model_icon = 'fa fa-address-book'

class projectAdmin(object):
    list_display = [
        'project_id',
        'name',
        # 'owner_id',
        'info',
        "contract",
        "phone_no",
        "wx",
        "email",
        "reg_date",
        "address",
        "longitude",
        "latitude"]
    search_fields = [
        'project_id',
        'name',
        # 'owner_id',
        'info',
        "contract",
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    list_filter = [
        'project_id',
        'name',
        # 'owner_id',
        'info',
        "contract",
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    model_icon = 'fa fa-cubes'

class vendorAdmin(object):
    list_display = [
        'vendor_id',
        'name',
        'info',
        'contract',
        "phone_no",
        "wx",
        "email",
        "reg_date",
        "address",
        "longitude",
        "latitude"]
    search_fields = [
        'vendor_id',
        'name',
        'info',
        'contract',
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    list_filter = [
        'vendor_id',
        'name',
        'info',
        'contract',
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    model_icon = 'fa fa-fax'

class designAdmin(object):
    list_display = [
        'design_id',
        'name',
        'info',
        'contract',
        "phone_no",
        "wx",
        "email",
        "reg_date",
        "address",
        "longitude",
        "latitude"]
    search_fields = [
        'design_id',
        'name',
        'info',
        'contract',
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    list_filter = [
        'design_id',
        'name',
        'info',
        'contract',
        "phone_no",
        "wx",
        "email",
        "address",
        "longitude",
        "latitude"]
    model_icon = 'fa fa-pencil'


# 将管理器与model进行注册关联
xadmin.site.register(smartpipe, smartpipeAdmin)
# xadmin.site.register(mqttmsg, mqttmsgAdmin)
xadmin.site.register(pipedetail, pipedetailAdmin)
xadmin.site.register(workorder, workorderAdmin)
xadmin.site.register(alert, alertAdmin)
# xadmin.site.register(po, poAdmin)
# xadmin.site.register(owner, ownerAdmin)
xadmin.site.register(project, projectAdmin)
xadmin.site.register(vendor, vendorAdmin)
xadmin.site.register(design, designAdmin)
