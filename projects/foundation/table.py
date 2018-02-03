# -*- coding: utf-8 -*-

from django.db import models


class Table(object):
    """
    database table
    """
    @classmethod
    def get_data(cls, key):
        if not isinstance(cls, models.Model):
            return None
        result = cls.objects.filter(id=key)
        if len(result) > 0:
            return result[0]
        else:
            return None

    @classmethod
    def has_data(cls, key):
        if not isinstance(cls, models.Model):
            return None

        result = cls.objects.filter(id=key)
        return len(result) > 0

    def __str__(self):
        if isinstance(self, models.Model):
            return self.id
        return ""

