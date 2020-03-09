from __future__ import unicode_literals
# encoding: utf-8
import math

from django.shortcuts import render

from django.shortcuts import HttpResponse

from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D
from pyecharts import Geo
from pyecharts import GeoLines, Style
from pyecharts import Map
from pyecharts import Gauge
from pyecharts import Bar, Line, Scatter, EffectScatter, Grid, Kline

# Create your views here.
#
# def index(request):
#     # request.POST
#     # requst.GET
#
#     return HttpResponse("My test -- steve_wei !")

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

#
# def test2(request):
#     template = loader.get_template('myfirstvis/pyecharts.html')
#
#     style = Style(
#         title_top="#fff",
#         title_pos="center",
#         width=1200,
#         height=600,
#         background_color="#404a59"
#     )
#
#     data_guangzhou = [
#         ["广州", "上海"],
#         ["广州", "北京"],
#         ["广州", "南京"],
#         ["广州", "重庆"],
#         ["广州", "兰州"],
#         ["广州", "杭州"]
#     ]
#     geolines = GeoLines("水务地图可视化--点线图", **style.init_style)
#     geolines.add("从广州出发", data_guangzhou, is_legend_show=False)
#
#     context = dict(
#         myechart=geolines.render_embed(),
#         host=REMOTE_HOST,
#         script_list=geolines.get_js_dependencies()
#     )
#     return HttpResponse(template.render(context, request))


def buy(request):
    return HttpResponse('Good by!')
