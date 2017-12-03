# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from crawler.models import Article
from crawler.serializers import ArticleSerializer
from rest_framework import viewsets


# Create your views here.
class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def base(request):
    return render(request, 'base.html')
