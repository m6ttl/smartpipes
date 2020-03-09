__author__ = 'Ò×Î¬¿Æ¼¼'

import xadmin
from mdeditor.fields import MDTextField
from .models import Comment


class CommentAdmin(object):
    list_display = ['user', 'article', 'text', 'create_time', 'parent']
    search_fields = ['user', 'article', 'text', 'parent']
    list_filter = ['user__username', 'article__title', 'text', 'create_time', 'parent']
    #field = ['user__username', 'article_title']
    ordering = ['user', 'article']

    # markdown
    style_fields = {"text": "MDTextField"}

xadmin.site.register(Comment, CommentAdmin)
