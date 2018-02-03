# -*- coding:utf-8 -*-

from functools import wraps

def singleton(cls):
    __instances = { }

    @wraps(cls)
    def instance(*args, **kw):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kw)
        return __instances[cls]

    return instance
