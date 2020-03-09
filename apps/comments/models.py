#coding:utf8
from django.db import models
from django.conf import settings
# from blog.models import Article
from datetime import datetime
from mdeditor.fields import MDTextField
# from django_markdown.models import MarkdownField
# Create your models here.


class Comment(models.Model):
    CM_CHOICES = (
        ("fk", u"反馈"),
        ("zx", u"咨询"),
        ("jy", u"建议")
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name=u'用户')
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name=u'文章')
    # text = models.TextField(verbose_name=u'交流')

    # text = models.MarkdownField(verbose_name=u'交流')

    text = models.MDTextField(verbose_name=u'交流XXX')

    kind = models.CharField(choices=CM_CHOICES, max_length=2, verbose_name=u"类型", default = 'fk')
    is_removed = models.BooleanField(default=False)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,default=None,blank=True,null=True,verbose_name=u'父交流')
    likes_count = models.PositiveIntegerField(default=0,verbose_name=u'点赞数')

    create_time = models.DateTimeField(verbose_name=u'创建时间', default=datetime.now)
    update_time = models.DateTimeField(verbose_name=u'修改时间', blank=True, null=True)

    class Meta:
        verbose_name = u'交流'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return self.article.title