# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from account.apps import AccountConfig
from foundation.table import Table

# Create your models here.

class User (models.Model, Table):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=True, null=True)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    qq = models.CharField(max_length=50, blank=True, null=True)
    webchat = models.CharField(max_length=50, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    googleplay = models.CharField(max_length=50, blank=True, null=True)
    appstore = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def is_pwd_right(username, pwd):
        result = User.objects.filter(name=username, password=pwd)
        return len(result) > 0

    class Meta:
        app_label = AccountConfig.name


class UserStatus(models.Model, Table):
    USER_STATUS = (
        (u'0', u'LogOut'),
        (u'1', u'LogIn'),
    )

    status = models.CharField(max_length=10, choices=USER_STATUS)
    datetime = models.DateTimeField()

    class Meta:
        app_label = AccountConfig.name

