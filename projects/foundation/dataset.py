# -*- coding:utf-8 -*-


class Container:
    def __init__(self):
        pass

    def clear(self):
        pass

    def data(self):
        pass


class Dictionary(Container):
    """
     key-value set
    """
    def __init__(self, **kwargs):
        Container.__init__(self)

        self._kwargs = {}
        self.flush(**kwargs)

    def clear(self):
        self._kwargs = {}

    def flush(self, **kwargs):
        for (k, v) in kwargs:
            self._kwargs[k] = v

    def filter(self):
        kwargs = {}
        for k in self._kwargs:
            if self._kwargs[k] is not None and self._kwargs[k] != '':
                kwargs[k] = self._kwargs[k]
        self._kwargs = kwargs

    def set(self, name, value):
        self._kwargs[name] = value

    def get(self, name, default=None):
        if name in self._kwargs:
            return self._kwargs[name]
        return default

    def has(self, *names):
        for k in names:
            if k not in self._kwargs:
                return False

        return True

    def remove(self, name):
        if name in self._kwargs:
            del self._kwargs[name]

    def data(self):
        return self._kwargs


class List(Container):
    """
    value set
    """
    def __init__(self, *args):
        Container.__init__(self)

        self._args = []
        self.flush(*args)

    def clear(self):
        self._args = []

    def flush(self, *args):
        for k in args:
            self._args.append(k)

    def filter(self):
        args = []
        for k in self._args:
            if k is not None and k != '':
                args.append(k)
        self._args = args

    def add(self, k):
        self._args.append(k)

    def remove(self, k):
        self._args.remove(k)

    def has(self, *keys):
        for k in keys:
            if k not in self._args:
                return False

        return True

    def data(self):
        return self._args

