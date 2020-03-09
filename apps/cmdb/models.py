from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    sex = models.CharField(verbose_name='性别', max_length=50)
    age = models.IntegerField(verbose_name='年龄')
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    enter_date = models.DateField(verbose_name='入学时间')
    remarks = models.TextField(verbose_name='备注', blank=True)

