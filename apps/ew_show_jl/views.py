from django.shortcuts import render

# Create your views here.
# @LoginValid
def index(request):
    return render(request, "ew_show_jl/index.html", locals())
def swwl(request):
    return render(request, "ew_show_jl/swwl.html", locals())
def dma(request):
    return render(request, "ew_show_jl/dma.html", locals())
def baoguanfenxi(request):
    return render(request, "ew_show_jl/baoguanfenxi.html", locals())

def gw(request):
    return render(request, "ew_show_jl/gw.html", locals())

def sp(request):
    return render(request, "ew_show_jl/sp.html", locals())

def css(request):
    return render(request, "ew_show_jl/css.html", locals())

def zhgj(request):
    return render(request, "ew_show_jl/zhgj.html", locals())

