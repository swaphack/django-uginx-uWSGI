# -*- coding: utf-8 -*-

from main.control.index import HomeLogic


def index(request):
    return HomeLogic.dispatch('id', request)


