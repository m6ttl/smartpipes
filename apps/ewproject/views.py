#coding:utf8
from django.shortcuts import render
from django.views.generic.base import View
from ewproject.models import *
from courses.models import Course
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class ewprojectView(View):
    def get(self, request):
        # # all_course = Course.objects.all()
        # ewprojects = ewProject.objects.all()  #将ewproject表中的所有对象赋值给users这个变量，它是一个列表
        # return render(request, 'ewproject.html', {'ewprojects': ewprojects}) #生成一个ewproject变量，这个变量可以给templates中的html文件使用

        return HttpResponse('Hello, World!')  #OK


class helloView(View):
    def get(self, request):
        return HttpResponse('Hello, World!')

class know1View(View):
    def get(self, request):
        return render(request, '智慧管件平台分析报告20181112_out.html')

class htmlsubView(View):
    def get(self, request):
        return render(request, 'ewproject/任务单201812_out.html')

class listcostView(View):
    def get(self, request):
        all_course = ewProject.objects.all()
        courses = Paginator(all_course, 20, request=request)
        return render(request, "ewproject/cost.html", {"all_course": courses })



class ReportListView(View):
    login_url = '/login/'
    redirect_field_name = 'next'
    def get(self, request):
        all_reports = ewReport.objects.all().order_by('-build_date')
        # reports = Paginator(all_reports, 20, request=request)
        return render(request, "report.html", {"all_reports": all_reports })

# class ReportInfoView(LoginRequiredMixin, View):
#     login_url = '/login/'
#     redirect_field_name = 'next'
#     def get(self, request, course_id):
#         # 此处的id为表默认为我们添加的值。
#         course = Course.objects.get(id=int(course_id))
#
#         # 查询用户是否开始学习了该课，如果还未学习则，加入用户课程表
#         user_courses = UserCourse.objects.filter(user= request.user, course= course)
#         if not user_courses:
#             user_course = UserCourse(user= request.user, course= course)
#             course.students +=1
#             course.save()
#             user_course.save()
#         # 查询课程资源
#         all_resources = CourseResource.objects.filter(course=course)
#         # 选出学了这门课的学生关系
#         user_courses = UserCourse.objects.filter(course= course)
#         # 从关系中取出user_id
#         user_ids = [user_course.user_id for user_course in user_courses]
#         # 这些用户学了的课程,外键会自动有id，取到字段
#         all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
#         # 取出所有课程id
#         course_ids = [user_course.course_id for user_course in all_user_courses]
#         # 获取学过该课程用户学过的其他课程
#         relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums").exclude(id =course.id)[:4]
#         # 是否收藏课程
#         return render(request, "course-video.html", {
#             "course": course,
#             "all_resources": all_resources,
#             "relate_courses":relate_courses,
#         })