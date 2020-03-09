# coding : utf-8
from datetime import datetime

from django.db import models

# Create your models here.


# 分类字典
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"服务机构")
    # 分类描述：备用不一定展示出来
    desc = models.CharField(max_length=200, verbose_name=u"描述")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"服务机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程类型
class CourseOrg(models.Model):
    DEGREE_CHOICES = (
        ("A", u"A新兵营"),
        ("B", u"B十八般兵器"),
        ("C", u"C货好不难卖"),
        ("D", u"D武功密籍"),
        ("E", u"E江湖风云录")
    )
    name = models.CharField(max_length=50, verbose_name=u"类型名称")
    # 类型描述，后面会替换为富文本展示
    desc = models.TextField(verbose_name=u"类型描述")
    # 类型类别:
    category = models.CharField(max_length=100, verbose_name=u"类型试题")
    tag = models.CharField(choices=DEGREE_CHOICES, max_length=10, verbose_name=u"类型标签")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(
        upload_to="org/%Y/%m",
        verbose_name=u"Logo",
        max_length=100)
    address = models.CharField(max_length=1050, verbose_name=u"地址")
    # 一个服务机构可以有很多课程类型，通过将city设置外键，变成课程类型的一个字段
    # 可以让我们通过类型找到分类
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name=u"服务机构")
    # 当学生点击学习课程，找到所属类型，学习人数加1
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    # 当发布课程就加1
    course_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "课程类型: {0}".format(self.name)


# 专家
class Teacher(models.Model):
    # 一个类型会有很多老师，所以我们在专家表添加外键并把课程类型名称保存下来
    # 可以使我们通过专家找到对应的类型
    org = models.ForeignKey(CourseOrg,  on_delete=models.CASCADE, verbose_name=u"所属类型")
    name = models.CharField(max_length=50, verbose_name=u"专家名称")
    work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"专长")
    work_position = models.CharField(max_length=50, verbose_name=u"江湖称号")
    email = models.EmailField(max_length=50, default="1@ewide.net", verbose_name=u"邮箱")
    age = models.IntegerField(default=18, verbose_name=u"年龄")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
    image = models.ImageField(
        default= '',
        upload_to="teacher/%Y/%m",
        verbose_name=u"头像",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"专家"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "[{0}]的专家: {1}".format(self.org, self.name)
