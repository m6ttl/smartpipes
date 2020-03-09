"""knowledge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django
from django.contrib import admin
from django.urls import path, include, re_path
# 导入x admin，替换admin
from django.views.static import serve
from django.conf.urls import url
from dashing.utils import router

# from knowledge.settings import MEDIA_ROOT
from ckeditor_uploader import urls as ckeditor_uploader_urls

import users
import xadmin
from django.views.generic import TemplateView
# from users.views import user_login
# from knowledge.settings import MEDIA_ROOT
from knowledge.settings import MEDIA_ROOT

from organization.views import OrgView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, \
    IndexView
# from ew_show_app.views import ew_show_appView

# from cmdb.views import EchartView

# from myechart import EchartView01
# from smartpipe.views import index
from smartpipe import views

# from blog.views import IndexView, ArticleDetailView,CategoryView,TagView
# from scen.views import EchartView

from .widgets import NewClientsWidget
router.register(NewClientsWidget, 'new_users_widget')

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # TemplateView.as_view会将template转换为view
    #path('', TemplateView.as_view(template_name= "index.html"), name=  "index"),

    path('blank/', TemplateView.as_view(template_name= "blank.html"), name=  "blank"),
    path('test/', TemplateView.as_view(template_name= "test.html"), name=  "test"),

    # path('', IndexView.as_view(), name=  "index"),
    path('index', IndexView.as_view(), name="index"),
    path('', views.index, name='home'),

    # url(r'index', index),
    # 基于类方法实现登录,这里是调用它的方法
    path('login/', LoginView.as_view(), name="login"),

    # 退出功能url
    path('logout/', LogoutView.as_view(), name="logout"),

    # 注册url
    path("register/", RegisterView.as_view(), name = "register" ),

    # 验证码url
    path("captcha/", include('captcha.urls')),

    # 激活用户url
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name= "user_active"),

    # 忘记密码
    path('forget/', ForgetPwdView.as_view(), name= "forget_pwd"),

    # 重置密码urlc ：用来接收来自邮箱的重置链接
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),

    # 修改密码url; 用于passwordreset页面提交表单
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),

    #驾驶舱
    url(r'^dashboard/', include(router.urls)),
    # url(r'^dashboard/', include(dashing.urls)),

    # 知识分类app的url配置，类型的也在里面
    path("org/", include('organization.urls', namespace='org')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    # re_path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),
    # 产品app的url配置
    path("course/", include('courses.urls', namespace="course")),
    # user app的url配置
    path("users/", include('users.urls', namespace="users")),

    # ew_show_app
    path("ew_show_app/", include('ew_show_app.urls')),

    # smartpipe
    path("smartpipe/", include('smartpipe.urls')),
    
    # scen
    # path("scen/", include('scen.urls', namespace="scen")),
    path("scen/", include('scen.urls')),

    # map
    path("map/", include('map.urls')),

    # # ew_show_app的url配置
    # path("ew_show_app/", include('ew_show_app.urls', namespace="ew_show_app")),

    # demosite的url配置
    # path("DemoSite/", views.index()),
    # url(r'^DemoSite/$',views.index),

    # # echart app的url配置
    # path("echart/", include('myecmdb.urls', namespace="echart")),

    # blog app的url配置
    # path("blog/", include('blog.urls', namespace="blog")),    #  app的url配置
    # path("", include('comments.urls', namespace="comments")),    #  app的url配置
    # path("", include('search.urls', namespace="search")),

    path('ew_show_jl/', include('ew_show_jl.urls')),

    # cmdb app的url配置
    # path("cmdb/", include('cmdb.urls', namespace="cmdb")),

    # path('echart01', EchartView01.echart01, name="echart01"),
    # xxproject app的url配置
    # path("xxproject/", include('xxproject.urls', namespace="xxproject")),

    # ewproject app的url配置
    # path("ewproject/", include('ewproject.urls', namespace="ewproject")),

    # demo app的url配置
    # path("demo/", include('demo.urls', namespace="demo")),

    # path('ew1', views.echart1, name="echart"),
    # path('echart1/', views.echart1),
    # path('ewide2/', views.ewide2),
    # path('ewide3/', views.ewide3),
    # path('ewide4/', views.ewide4),
    # path('ewide5/', views.ewide5),

    # path('building/', views.building),

    # path('test001/', include('test001.urls')),
    # path('test001/', test001),
    # path('echart2/', myfirstvis.urls),

    # user app的url配置
    # path("ewtest/", include('ewtest.urls', namespace="ewtest")),
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
    path('mdeditor/', include('mdeditor.urls')),
]
