# -*- coding: utf-8 -*-

from foundation.control import LogicEvent
from foundation.factory import Singleton
from main.page.index import HomePage


class HomeLogic(LogicEvent):
    def __init__(self):
        LogicEvent.__init__(self)

    @classmethod
    def index(cls, request):
        return HomePage.flush(request)

    @staticmethod
    def page(request, params):
        pass




