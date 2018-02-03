# -*- coding:utf-8 -*-

from foundation.tools import get_params
from dataset import Dictionary
from foundation.html import HTMLNode
from django.shortcuts import render


class LogicEvent:
    """
    逻辑处理
    """
    def __init__(self):
        pass

    @classmethod
    def hand_logic(cls, params, key, request):
        """
        处理逻辑
        :param params:
        :param key:
        :param request:
        :return:
        """
        if not params.has(key):
            return cls.index(request)

        method = params.get(key)
        if not hasattr(cls, method):
            raise Exception

        params.remove(key)
        handler = getattr(cls, method)
        if handler is None:
            raise Exception

        return handler(request, params)

    @classmethod
    def dispatch(cls, key, request):
        if key is None or request is None:
            raise Exception

        kwargs = get_params(request)

        params = Dictionary()
        for k in kwargs:
            params.set(k, kwargs[k])
        params.filter()

        return cls.hand_logic(params, key, request)

    @classmethod
    def index(cls, request):
        """
        重写改函数，处理无效操作参数
        :param request:
        :return:
        """
        pass

########################################################################


class PageTemplate:
    """
    template page
    """
    def __init__(self):

        self.__header = HTMLNode()
        self.__header.set_name('header')

        self.__content = HTMLNode()
        self.__content.set_name('content')

        self.__footer = HTMLNode()
        self.__footer.set_name('footer')

    def get_header(self):
        """
        get template header node
        :return:
        """
        return self.__header

    def get_content(self):
        """
        get template content node
        :return:
        """
        return self.__content

    def get_footer(self):
        """
        get template footer node
        :return:
        """
        return self.__footer

    def get_context(self):
        context = HTMLNode()
        context.set_name('ui')
        context.set_attr('header', self.get_header().data())
        context.set_attr('content', self.get_content().data())
        context.set_attr('footer', self.get_footer().data())
        return context.data()


class ViewPage:
    """
    define base class for view page
    """
    template_name = None

    def __init__(self):
        pass

    @classmethod
    def flush(cls, request):
        """
        flush view page with self define data
        :param request:
        :return:
        """
        context = PageTemplate()
        cls.init_context(request, context)
        body = context.get_context()
        return render(request, cls.template_name, body)

    @classmethod
    def init_context(cls, request, context):
        """
        override this function or use default value
        """
        pass
