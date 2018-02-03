# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from resources.control.db import ResDB

# Create your views here.


def index(request):
    return ResDB.singleton().dispatch('id', request)

