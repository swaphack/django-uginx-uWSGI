# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from account.models import *

admin.site.register(User)
admin.site.register(UserStatus)