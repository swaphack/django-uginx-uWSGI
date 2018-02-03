# -*- coding: utf-8 -*-


def partial(**outer_kwargs):
    def wrapper(func):
        def inner(*args, **kwargs):
            for k, v in outer_kwargs.items():
                kwargs[k] = v
            return func(*args, **kwargs)
        return inner
    return wrapper


def enum(*sequential, **named):
    """
    enum
    :param sequential:
    :param named:
    :return:
    """
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

