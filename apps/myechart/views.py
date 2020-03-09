from __future__ import unicode_literals
# encoding: utf-8
import math

from django.shortcuts import render
from django.views.generic import View

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
def building(request):
    # request.POST
    # requst.GET

    return HttpResponse("功能建设中，等着!")

REMOTE_HOST = "https://pyecharts.github.io/assets/js"

class EchartView01(View):
    def echart(self, requset):
        template = loader.get_template('ewpyecharts.html')

        line = Line("合同分析", width=1200, height=700)
        attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        line.add("最高压力", attr, [11, 11, 15, 13, 12, 13, 10],
                 mark_point=["max", "min"], mark_line=["average"])
        line.add("最低压力", attr, [1, -2, 2, 5, 3, 2, 0],
                 mark_point=["max", "min"], legend_top="50%", mark_line=["average"],
                 # 设置 dataZoom 控制索引为 0,1 的 x 轴，即第一个和第二个
                 is_datazoom_show=True, datazoom_xaxis_index=[0, 1])

        v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
              [2300, 2291.3, 2288.26, 2308.38],
              [2295.35, 2346.5, 2295.35, 2345.92],
              [2347.22, 2358.98, 2337.35, 2363.8],
              [2360.75, 2382.48, 2347.89, 2383.76],
              [2383.43, 2385.42, 2371.23, 2391.82],
              [2377.41, 2419.02, 2369.57, 2421.15],
              [2425.92, 2428.15, 2417.58, 2440.38],
              [2411, 2433.13, 2403.3, 2437.42],
              [2432.68, 2334.48, 2427.7, 2441.73],
              [2430.69, 2418.53, 2394.22, 2433.89],
              [2416.62, 2432.4, 2414.4, 2443.03],
              [2441.91, 2421.56, 2418.43, 2444.8],
              [2420.26, 2382.91, 2373.53, 2427.07],
              [2383.49, 2397.18, 2370.61, 2397.94],
              [2378.82, 2325.95, 2309.17, 2378.82],
              [2322.94, 2314.16, 2308.76, 2330.88],
              [2320.62, 2325.82, 2315.01, 2338.78],
              [2313.74, 2293.34, 2289.89, 2340.71],
              [2297.77, 2313.22, 2292.03, 2324.63],
              [2322.32, 2365.59, 2308.92, 2366.16],
              [2364.54, 2359.51, 2330.86, 2369.65],
              [2332.08, 2273.4, 2259.25, 2333.54],
              [2274.81, 2326.31, 2270.1, 2328.14],
              [2333.61, 2347.18, 2321.6, 2351.44],
              [2340.44, 2324.29, 2304.27, 2352.02],
              [2326.42, 2318.61, 2314.59, 2333.67],
              [2314.68, 2310.59, 2296.58, 2320.96],
              [2309.16, 2286.6, 2264.83, 2333.29],
              [2282.17, 2263.97, 2253.25, 2286.33],
              [2255.77, 2270.28, 2253.31, 2276.22]]
        kline = Kline("考核表分析", title_top="50%")
        kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)],
                  v1, is_datazoom_show=True)

        grid = Grid()
        grid.add(line, grid_top="60%")
        grid.add(kline, grid_bottom="60%")
        #    grid.render()

        context = dict(
            myechart=grid.render_embed(),
            host=REMOTE_HOST,
            script_list=grid.get_js_dependencies()
        )

        return HttpResponse(template.render(context, request))


def echart01(request):
    template = loader.get_template('ewpyecharts.html')

    line = Line("压力分析", width=1200, height=700)
    attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    line.add("最高压力", attr, [11, 11, 15, 13, 12, 13, 10],
             mark_point=["max", "min"], mark_line=["average"])
    line.add("最低压力", attr, [1, -2, 2, 5, 3, 2, 0],
             mark_point=["max", "min"], legend_top="50%", mark_line=["average"],
             # 设置 dataZoom 控制索引为 0,1 的 x 轴，即第一个和第二个
             is_datazoom_show=True, datazoom_xaxis_index=[0, 1])

    v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
          [2300, 2291.3, 2288.26, 2308.38],
          [2295.35, 2346.5, 2295.35, 2345.92],
          [2347.22, 2358.98, 2337.35, 2363.8],
          [2360.75, 2382.48, 2347.89, 2383.76],
          [2383.43, 2385.42, 2371.23, 2391.82],
          [2377.41, 2419.02, 2369.57, 2421.15],
          [2425.92, 2428.15, 2417.58, 2440.38],
          [2411, 2433.13, 2403.3, 2437.42],
          [2432.68, 2334.48, 2427.7, 2441.73],
          [2430.69, 2418.53, 2394.22, 2433.89],
          [2416.62, 2432.4, 2414.4, 2443.03],
          [2441.91, 2421.56, 2418.43, 2444.8],
          [2420.26, 2382.91, 2373.53, 2427.07],
          [2383.49, 2397.18, 2370.61, 2397.94],
          [2378.82, 2325.95, 2309.17, 2378.82],
          [2322.94, 2314.16, 2308.76, 2330.88],
          [2320.62, 2325.82, 2315.01, 2338.78],
          [2313.74, 2293.34, 2289.89, 2340.71],
          [2297.77, 2313.22, 2292.03, 2324.63],
          [2322.32, 2365.59, 2308.92, 2366.16],
          [2364.54, 2359.51, 2330.86, 2369.65],
          [2332.08, 2273.4, 2259.25, 2333.54],
          [2274.81, 2326.31, 2270.1, 2328.14],
          [2333.61, 2347.18, 2321.6, 2351.44],
          [2340.44, 2324.29, 2304.27, 2352.02],
          [2326.42, 2318.61, 2314.59, 2333.67],
          [2314.68, 2310.59, 2296.58, 2320.96],
          [2309.16, 2286.6, 2264.83, 2333.29],
          [2282.17, 2263.97, 2253.25, 2286.33],
          [2255.77, 2270.28, 2253.31, 2276.22]]
    kline = Kline("考核表分析", title_top="50%")
    kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)],
              v1, is_datazoom_show=True)

    grid = Grid()
    grid.add(line, grid_top="60%")
    grid.add(kline, grid_bottom="60%")
#    grid.render()

    context = dict(
        myechart=grid.render_embed(),
        host=REMOTE_HOST,
        script_list=grid.get_js_dependencies()
    )

    return HttpResponse(template.render(context, request))


def ewide2(request):
    template = loader.get_template('ewpyecharts.html')

    style = Style(
        title_top="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59"
    )

    data_guangzhou = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]
    ]
    geolines = GeoLines("水务地图可视化--点线图", **style.init_style)
    geolines.add("从广州出发", data_guangzhou, is_legend_show=False)

    context = dict(
        myechart=geolines.render_embed(),
        host=REMOTE_HOST,
        script_list=geolines.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))


def ewide3(request):
    template = loader.get_template('ewpyecharts.html')

    value = [20, 190, 253, 77, 65]
    attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
    map = Map("水务数据可视化--产销差筛选钻取", width=1200, height=600)
    map.add("", attr, value, maptype='广东', is_visualmap=True,
            visual_text_color='#000')
    map.render()
    context = dict(
        myechart=map.render_embed(),
        host=REMOTE_HOST,
        script_list=map.get_js_dependencies()
    )

    gauge = Gauge("水务数据可视化")
    gauge.add("产销差", "完成率", 66.66)
    gauge.show_config()

    return HttpResponse(template.render(context, request))

def ewide4(request):
    # gauge = Gauge("仪表盘示例")
    # gauge.add("业务指标", "完成率", 66.66)
    # gauge.show_config()
    template = loader.get_template('ewpyecharts.html')
    data = [
        ('北京', 28), ('天津', 29), ('石家庄', 29), ('太原', 34), ('呼和浩特', 27), ('哈尔滨', 31), ('长春', 29), ('沈阳', 30), ('上海', 40),
        ('合肥', 40), ('南京', 40), ('济南', 35), ('青岛', 33), ('杭州', 40), ('福州', 37), ('厦门', 34), ('南昌', 39), ('武汉', 38),
        ('长沙', 39),
        ('郑州', 37), ('南宁', 36), ('广州', 33), ('深圳', 28), ('珠海', 30), ('海口', 30), ('三亚', 31), ('西安', 39), ('兰州', 32),
        ('乌鲁木齐', 31),
        ('西宁', 27), ('银川', 30), ('成都', 32), ('重庆', 38), ('贵阳', 29), ('昆明', 22), ('拉萨', 23), ('香港', 30), ('澳门', 30), ]
    #
    # geo = Geo("7月23日全国主要城市最高气温", "数据源自中国天气网", title_color="#000000", title_pos="center",
    #           width=1200, height=600, background_color='#FFFFFF')
    # attr, value = geo.cast(data)
    # geo.add("", attr, value, visual_range=[20, 40], visual_text_color="#000000", symbol_size=15, is_visualmap=True)
    # geo.show_config()

    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff",
              title_pos="center", width=1200,
              height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 300],
            visual_text_color='#fff')

    # data = [
    #     ('汕头市', 50), ('汕尾市', 60), ('揭阳市', 35),
    #     ('阳江市', 44), ('肇庆市', 72)
    # ]
    # geo = Geo("广东城市空气质量", "data from pm2.5", title_color="#fff",
    #           title_pos="center", width=1200,
    #           height=600, background_color='#404a59')
    # attr, value = geo.cast(data)
    # geo.add("", attr, value, maptype='广东', type="effectScatter",
    #         is_random=True, effect_scale=5, is_legend_show=False)
    # # geo.show_config()

    context = dict(
        myechart=geo.render_embed(),
        host=REMOTE_HOST,
        script_list=geo.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

def ewide5(request):

    template = loader.get_template('ewpyecharts.html')
    style = Style(
        title_top="#fff",
        title_pos="center",
        width=1200,
        height=600,
        background_color="#404a59"
    )
    style_geo = style.add(
        is_label_show=True,
        line_curve=0.2,
        line_opacity=0.6,
        legend_text_color="#eee",
        legend_pos="right",
        geo_effect_symbol="plane",
        geo_effect_symbolsize=15,
        label_color=['#a6c84c', '#ffa022', '#46bee9'],
        label_pos="right",
        label_formatter="{b}",
        label_text_color="#eee",
    )
    data_guangzhou = [
        ["广州", "上海"],
        ["广州", "北京"],
        ["广州", "南京"],
        ["广州", "重庆"],
        ["广州", "兰州"],
        ["广州", "杭州"]
    ]
    data_beijing = [
        ["北京", "上海"],
        ["北京", "广州"],
        ["北京", "南京"],
        ["北京", "重庆"],
        ["北京", "兰州"],
        ["北京", "杭州"]
    ]
    geolines1 = GeoLines("GeoLines 示例", **style.init_style)
    geolines1.add("从广州出发", data_guangzhou, **style_geo)
    geolines1.add("从北京出发", data_beijing, **style_geo)

    # geo.show_config()
    context = dict(
        myechart=geolines1.render_embed(),
        host=REMOTE_HOST,
        script_list=geolines1.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))



def index(request):
    template = loader.get_template('ewpyecharts.html')
    l3d = line3d()
    context = dict(
        myechart=l3d.render_embed(),
        host=REMOTE_HOST,
        script_list=l3d.get_js_dependencies()
    )
    return HttpResponse(template.render(context, request))

# def map1():
#     value = [20, 190, 253, 77, 65]
#     attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市']
#     map = Map("广东地图示例", width=1200, height=600)
#     map.add("", attr, value, maptype='广东', is_visualmap=True,
#             visual_text_color='#000')
#     #map.render()
#     return map


def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    return line3d


# def index(request):
#     # request.POST
#     # requst.GETtest
#
#     return HttpResponse("My test test -- steve_wei !" )

# def test(request):
#     # request.POST
#     # requst.GETtest
#
#     return HttpResponse("just test -- steve_wei !" )

def test(request):
    # request.POST
    # requst.GETtest

    return HttpResponse("just test -- steve_wei !" )


# def ewide4(request):
# data = [
#     ('北京',28),('天津',29),('石家庄',29),('太原',34),('呼和浩特',27),('哈尔滨',31),('长春',29),('沈阳',30),('上海',40),
#     ('合肥',40),('南京',40),('济南',35),('青岛',33),('杭州',40),('福州',37),('厦门',34),('南昌',39),('武汉',38),('长沙',39),
#     ('郑州',37),('南宁',36),('广州',33),('深圳',28),('珠海',30),('海口',30),('三亚',31),('西安',39),('兰州',32),('乌鲁木齐',31),
#     ('西宁',27),('银川',30),('成都',32),('重庆',38),('贵阳',29),('昆明',22),('拉萨',23),('香港',30),('澳门',30),]
#
# geo = Geo("7月23日全国主要城市最高气温", "数据源自中国天气网", title_color="#000000", title_pos="center",
# width=1200, height=600, background_color='#FFFFFF')
# attr, value = geo.cast(data)
# geo.add("", attr, value, visual_range=[20, 40], visual_text_color="#000000", symbol_size=15,is_visualmap=True)
# geo.show_config()
# geo.render()
#
# return HttpResponse("just test -- steve_wei !" )
# return geo
