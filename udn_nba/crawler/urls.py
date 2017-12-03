# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from crawler.views import ArticleViewSet, base
from rest_framework.urlpatterns import format_suffix_patterns

article_list = ArticleViewSet.as_view({'get': 'list'})
article_detail = ArticleViewSet.as_view({'get': 'retrieve'})

urlpatterns = format_suffix_patterns([
    url(r'^$', base),
    url('^articles/$', article_list, name='article_list'),
    url('^articles/(?P<pk>[0-9]+)/$', article_detail, name='article_detail'),
])