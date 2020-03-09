from datetime import datetime
from mdeditor.fields import MDTextField

# import mdeditor.fields

from django.db import models

# 引入我们CourseComments所需要的外键models
from users.models import UserProfile
from courses.models import Course


# Create your models here.


# 用户我要学习表单
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户: {0} 手机号: {1}'.format(self.name, self.mobile)

# 用户对于课程交流
class CourseComments(models.Model):
    CM_CHOICES = (
        ("pl", u"好评"),
        ("cp", u"差评"),
        ("zx", u"咨询"),
        ("jl", u"交流")
    )
    # 会涉及两个外键: 1. 用户， 2. 课程。import进来
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    # comments = models.CharField(max_length=250, verbose_name=u"交流")

    kind = models.CharField(choices=CM_CHOICES, max_length=2, verbose_name=u"类型", default = 'pl')
    ctitle = models.CharField(max_length=30, verbose_name="主题", default = '交流')
    comments = MDTextField(verbose_name=u"交流")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"交流时间")

    class Meta:
        verbose_name = u"课程交流"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})对于《{1}》 交流 :'.format(self.user, self.course)


# 用户对于课程,类型，专家的收藏
class UserFavorite(models.Model):
    # 会涉及四个外键。用户，课程，类型，专家import
    TYPE_CHOICES = (
        (1, u"课程"),
        (2, u"课程类型"),
        (3, u"专家")
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    # course = models.ForeignKey(Course, verbose_name=u"课程")
    # teacher = models.ForeignKey()
    # org = models.ForeignKey()
    # fav_type =

    # 机智版
    # 直接保存用户的id.
    fav_id = models.IntegerField(default=0)
    # 表明收藏的是哪种类型。
    fav_type = models.IntegerField(
        choices=TYPE_CHOICES,
        default=1,
        verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"交流时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})收藏了{1} '.format(self.user, self.fav_type)

# 用户消息表
class UserMessage(models.Model):
        # 因为我们的消息有两种:发给全员和发给某一个用户。
        # 所以如果使用外键，每个消息会对应要有用户。很难实现全员消息。

        # 机智版 为0发给所有用户，不为0就是发给用户的id
    user = models.IntegerField(default=0, verbose_name=u"接收用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")

    # 是否已读: 布尔类型 BooleanField False未读,True表示已读
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})接收了{1} '.format(self.user, self.message)


# 用户课程表
class UserCourse(models.Model):
    # 会涉及两个外键: 1. 用户， 2. 课程。import进来
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"用户")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户({0})学习了{1} '.format(self.user, self.course)
