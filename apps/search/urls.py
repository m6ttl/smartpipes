__author__ = 'Ò×Î¬¿Æ¼¼'


from django.conf.urls import url, include
from search import views

urlpatterns = [
    url(r'^search/', views.search, name='search'),
]


