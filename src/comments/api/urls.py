from django.conf.urls import url
from django.contrib import admin

from .views import (
    CommentListAPIView,
    CommentDetailAPIView

    )

urlpatterns = [
    url('^$',CommentListAPIView.as_view(),name='list'),
    url(r'^(?P<pk>\d+)/$', CommentDetailAPIView, name='thread'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
