# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from book.page.index import MainPage

# Create your views here.


def index(request):
    return MainPage.flush(request)
