# encoding: utf-8
__author__ = '易维科技'
__date__ = '2018/1/13 0013 01:57'

# encoding: utf-8
from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView
from courses.views import CourseListMView
from django.urls import path, re_path

app_name = "courses"
urlpatterns = [
    # 课程列表url
    path('list/', CourseListView.as_view(), name="list"),
    # 移動端
    path('listm/', CourseListMView.as_view(), name="listm"),

    # 课程详情页
    re_path('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),
    # 课程章节信息页
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),

# 课程章节信息页
    re_path('comments/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),

    # 添加课程交流,已经把参数放到post当中了
    path('add_comment/', AddCommentsView.as_view(), name="add_comment"),


    # 课程视频播放页
    re_path('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),
]
