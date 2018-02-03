from foundation.control import LogicEvent
from foundation.tools import create_dict

from django.shortcuts import render
from account.models import User

class UserLogic(LogicEvent):
    def __init__(self):
        LogicEvent.__init__(self)

    def index(self, request):
        msg = create_dict()
        msg.set('login_url', 'user/')
        msg.set('username', 'username')
        msg.set('password', 'password')
        tbl = msg.data()
        return render(request, "account/login.html", tbl)

    def login(self, request, params):
        """
        :param request
        :param params: name password
        :return:
        """

        if not params.has('name', 'password'):
            raise Exception

        message = create_dict()
        message.set('title', "login success")

        result = User.is_pwd_right(params.get('name'), params.get('password'))
        if not result:
            message.set('body', "Name or Password is Error!")
        else:
            message.set('body', "Welcome to My WebSite!")

        return render(request, "message_box.html", message.data())

    def logout(self, request, params):
        """
        :param request
        :param params: id
        :return:
        """
        if params.has('id'):
            raise Exception

        result = User.objects.filter(params.data())

def index(request):
    return UserLogic.singleton().dispatch('id', request)






