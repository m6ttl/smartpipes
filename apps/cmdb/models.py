from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(verbose_name='ѧ������', max_length=50)
    sex = models.CharField(verbose_name='�Ա�', max_length=50)
    age = models.IntegerField(verbose_name='����')
    address = models.CharField(verbose_name='��ͥסַ', max_length=250, blank=True)
    enter_date = models.DateField(verbose_name='��ѧʱ��')
    remarks = models.TextField(verbose_name='��ע', blank=True)

