__author__ = 'Ò×Î¬¿Æ¼¼'


from django.conf.urls import url, include
from comments.views import CommentView

urlpatterns = [
    url(r'^comment/(?P<article_id>\d+)$', CommentView.as_view(), name='comment-view'),
]