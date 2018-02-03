from foundation.control import LogicEvent
from foundation.dataset import Dictionary

from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import render
from shop.tables.shop import Item

class ShopLogic(LogicEvent):
    def __init__(self):
        LogicEvent.__init__(self)

    def index(self, request):
        pass

    @staticmethod
    def pick(request, params):
        if not isinstance(params, Dictionary):
            return HttpResponseServerError()

        if not params.has('begin', 'end'):
            return HttpResponseBadRequest()

        result = Item.get_items(int(params.get('begin')), int(params.get('end')))
        return render(request, "shop/index.html", {'items': result})

def index(request):
    return ShopLogic.dispatch('id', request)
