# _*_ encoding:utf-8 _*_
from django.shortcuts import render

import json
from .models import smartpipe,pipedetail

from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from django.template import loader
from django.views.generic.base import View

#############
from random import randrange

from rest_framework.views import APIView

# import simplejson as json
import numpy as np
import pandas as pd
from pandas import DataFrame
import pymysql

# from __future__ import unicode_literals
# from pyecharts import Line, Pie, Grid, configure

from pyecharts.charts import Bar,Line, Pie, Grid

from pyecharts import options as opts
# configure(output_image=True)
# from pyecharts import online
# online() # 使用远程 jshost


from pandasql import sqldf
import time
from datetime import datetime
import datetime

from pyecharts.commons.utils import JsCode
from pyecharts.faker import Collector, Faker
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType,ThemeType
from pyecharts.charts import Bar, Grid, Line, Page, Pie, Geo,Liquid
import json
import os
from pyecharts.components import Table

from pyecharts import options as opts
from pyecharts.charts import Page, Tree

from pandas import DataFrame
import numpy as np
import pandas as pd

from pyecharts.components import Image
from pyecharts.options import ComponentTitleOpts

#############

conn = pymysql.connect(host='rm-uf6k42ke05jq7358so.mysql.rds.aliyuncs.com', port=3306, user='root_top', password='root_Top', db='smartpipe',
                       charset='utf8')

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)


def index(request):
    # address_point = gis_info.objects.filter( p_type == '1' )

    address_point = smartpipe.objects.all()

    address_longitude = []
    address_latitude = []
    address_data = []
    address_id = []

    for i in range(len(address_point)):
        address_longitude.append(address_point[i].longitude)
        address_latitude.append(address_point[i].latitude)
        address_data.append(address_point[i].name)
        address_id.append(address_point[i].id)

    return render(request, 'smartpipe/map_address.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude),
                   'address_data': json.dumps(address_data),
                   'address_id': json.dumps(address_id),

                   }
                )

class pipe(View):
    def get(self, request, meter_id):
        s_id = meter_id

        cursor = conn.cursor()
        # 基本情况
        sql_s = ("""
        select t.name, t.caliber, t.sn, t.depth, t.install_date, t.interface, t.pipeline  from smartpipe_smartpipe t where id = {}

        """.format(s_id))

        df_a1 = pd.read_sql(sql_s, conn)
        # df_a1

        s_name = df_a1['name'].iloc[0]  # "名称"
        s_caliber = df_a1['caliber'].iloc[0]  # "口径"
        s_sn = df_a1['sn'].iloc[0]  # "编号"


        # 	安装信息
        s_depth = df_a1['depth'].iloc[0]  # "埋深"
        s_install_date = df_a1['install_date'].iloc[0]  # "安装时间"
        s_interface = df_a1['interface'].iloc[0]  # "接口方式"
        s_pipeline = df_a1['pipeline'].iloc[0]  # "管道材质"

        # 最近工况

        sql_b1 = """
        select * from smartpipe_pipedetail where 
        pipe_id_id = {}
        and collection_time = (select max(collection_time) from smartpipe_pipedetail where pipe_id_id = {})""".format(
            s_id, s_id)

        df_b1 = pd.read_sql(sql_b1, conn)
        # df_b1

        s_collection_time = df_b1['collection_time'].iloc[0].strftime("%Y-%m-%d %H:%M:%S")  # "最近采集时间"
        s_pressure = df_b1['pressure'].iloc[0]  # "压力"
        s_ins_flow = df_b1['ins_flow'].iloc[0]  # "瞬间流量"
        s_tem = df_b1['tem'].iloc[0]  # "温度"
        s_power = df_b1['power'].iloc[0]  # "电力剩余情况"

        # 走势情况

        sql_c = ("""
        select * from smartpipe_pipedetail  where pipe_id_id = {} order by collection_time desc limit 30

        """.format(s_id))

        df_cl = pd.read_sql(sql_c, conn)
        # df_cl

        l_a = df_cl['collection_time'].astype(str).tolist()
        # l_a

        l_v1 = df_cl['pressure'].tolist()
        # l_v1

        l_v2 = df_cl['ins_flow'].tolist()
        # l_v2

        # 流量柱状图
        def bar_ll() -> Bar:
            c = (
                Bar()
                    .add_xaxis(l_a)
                    .add_yaxis("流量曲线", l_v2)
                    .set_series_opts(itemstyle_opts={
                    "normal": {
                        "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: 'rgba(0, 77, 167, 1)'
                        }, {
                            offset: 1,
                            color: 'rgba(0, 244, 255, 1)'
                        }], false)"""),
                        "shadowColor": 'rgb(0, 160, 221)',
                    }}
                )
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False, font_size=10),
                                     )

                    .set_global_opts(
                    title_opts=opts.TitleOpts(title=f" [ {s_name}] 近30次"),
                    xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30), ),  # 设置x轴标签旋转角度
                )
            )
            return c

        # bar_lc2().render_notebook()

        # 压力柱状图
        def bar_yl() -> Line:
            c = (
                Line()
                    .add_xaxis(l_a)
                    .add_yaxis("压力曲线", l_v1)
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False, font_size=10),
                                     )
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title=f" [ {s_name}]")
                )
            )
            return c

        # bar_lc1().render_notebook()
        context = dict(
            t_name=s_name,
            t_caliber=s_caliber,
            t_sn=s_sn,
            t_depth=s_depth,
            t_install_date=s_install_date,
            t_interface=s_interface,
            t_pipeline=s_pipeline,
            t_collection_time=s_collection_time,
            t_pressure=s_pressure,
            t_ins_flow=s_ins_flow,
            t_tem=s_tem,
            t_power=s_power,
            t_chart_yl=bar_yl().render_embed(),
            t_chart_ll=bar_ll().render_embed(),

        )

        template = loader.get_template('smartpipe/collectinfo.html')
        html_out = template.render(context, request)
        return HttpResponse(html_out)