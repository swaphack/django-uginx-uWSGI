# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from book.apps import BookConfig
# Create your models here.
app_name = BookConfig.name


class Book(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    author_id = models.IntegerField(blank=False, null=False)
    book_dir = models.CharField(max_length=100, blank=False, null=False)
    create_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = app_name

