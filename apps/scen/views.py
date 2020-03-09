#coding:utf8
from django.shortcuts import render
from django.views.generic.base import View
from scen.models import *
# from courses.models import Course
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# class scenView(View):
#     # login_url = '/login/'
#     redirect_field_name = 'next'
#     def get(self, request):
#         all_scenhtmls = scenhtml.objects.all().order_by('-build_date')
#         # reports = Paginator(all_reports, 20, request=request)
#         return render(request, "scen.html", {"all_scenhtmls": all_scenhtmls })

class scenView(View):
    login_url = '/login/'
    redirect_field_name = 'next'
    def get(self, request):
        all_reports = scenhtml.objects.all().order_by('-build_date')
        # reports = Paginator(all_reports, 20, request=request)
        return render(request, "scen.html", {"all_reports": all_reports })

