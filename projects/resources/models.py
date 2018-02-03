# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from resources.apps import ResourcesConfig
from django.db import models


app_name = ResourcesConfig.name


class Language(models.Model):
    """
    language defined
    """
    kind = models.IntegerField(blank=True, null=True)
    lang = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.lang

    class Meta:
        app_label = app_name


class Text(models.Model):
    """
    ui text, for different languages
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    cn = models.TextField(blank=True, null=True)
    en = models.TextField(blank=True, null=True)
    arb = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = app_name


class Resource(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    path = models.TextField(blank=True, null=True)

    def image_tag(self):
        return u'<img src="/static%s" />' % self.path

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        app_label = app_name
