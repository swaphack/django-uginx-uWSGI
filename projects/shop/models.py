# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from foundation.table import Table
from shop.apps import ShopConfig

# Create your models here.


class Item(models.Model, Table):
    name = models.CharField(max_length=50, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_items(start, end):
        items = Item.objects.all()
        count = len(items)
        if count == 0:
            return None
        else:
            if start > count:
                return None
            if end > count:
                return None

            return items[start:end]

    class Meta:
        app_label = ShopConfig.name
