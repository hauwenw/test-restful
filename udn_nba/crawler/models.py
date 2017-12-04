# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.CharField(validators=[URLValidator], max_length=200)
    url = models.CharField(validators=[URLValidator], max_length=200, unique=True)
    content = models.TextField()
    posted = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-posted', )


class Video(models.Model):
    article = models.ForeignKey(Article, related_name="videos", on_delete=models.CASCADE)
    source = models.CharField(validators=[URLValidator], max_length=200)
