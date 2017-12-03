# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from crawler.models import Article, Video

# Register your models here.
admin.site.register(Article)
admin.site.register(Video)
