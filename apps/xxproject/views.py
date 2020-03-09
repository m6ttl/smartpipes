#coding:utf8
from django.shortcuts import render
from django.views.generic.base import View
from xxproject.models import *
from courses.models import Course
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# class xxprojectView(View):
#     def get(self, request):
#         # # all_course = Course.objects.all()
#         # xxprojects = ewProject.objects.all()  #将xxproject表中的所有对象赋值给users这个变量，它是一个列表
#         # return render(request, 'xxproject.html', {'xxprojects': xxprojects}) #生成一个xxproject变量，这个变量可以给templates中的html文件使用
#
#         return HttpResponse('Hello, World!')  #OK

#
# class helloView(View):
#     def get(self, request):
#         return HttpResponse('Hello, World!')
#
# class know1View(View):
#     def get(self, request):
#         return render(request, '智慧管件平台分析报告20181112_out.html')
#
# class htmlsubView(View):
#     def get(self, request):
#         return render(request, 'xxproject/任务单201812_out.html')
#
# class listcostView(View):
#     def get(self, request):
#         all_course = ewProject.objects.all()
#         courses = Paginator(all_course, 20, request=request)
#         return render(request, "xxproject/cost.html", {"all_course": courses })
#
#
#
# class ReportListView(View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#     def get(self, request):
#         all_reports = ewReport.objects.all().order_by('-build_date')
#         # reports = Paginator(all_reports, 20, request=request)
#         return render(request, "report.html", {"all_reports": all_reports })
