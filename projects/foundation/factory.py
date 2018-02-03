# -*- coding:utf-8 -*-

from foundation import dataset


class Event:
    def __init__(self):
        self._events = dataset.Dictionary()

    def bind(self, name, handler):
        self._events.set(name, handler)

    def unbind(self, name):
        self._events.set(name, None)

    def hand_event(self, key, **params):
        """
        处理事件
        :param key:
        :param params:
        :return:
        """
        if not params.get(key):
            return

        method = params.get(key)
        if not self._events.has(method):
            return

        params.pop(key)
        handler = self._events.get(method)
        if handler is None:
            return

        handler(params)

    def dispatch(self, key, **params):
        self.hand_event(key, **params)


class Singleton:
    """
    single class instance
    """
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def singleton(cls):
        """
        单例
        :return:
        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

