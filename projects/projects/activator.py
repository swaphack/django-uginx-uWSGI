# -*- coding: utf-8 -*-

from django.http.response import HttpResponseNotFound, HttpResponse
import importlib
from main.views import index

def process_view(request, **kwargs):
    """
    process each app view
    :param request:
    :param kwargs:
    :return:
    """
    app = kwargs.get('app', None)
    if app is None:
        return index(request)
    try:
        viewObj = importlib.import_module("%s.views" % app)
        funcObj = getattr(viewObj, 'index')
        return funcObj(request)
    except (ImportError, AttributeError) as e:
        return HttpResponse(e)
        # return HttpResponseNotFound()
    except Exception as e:
        return HttpResponse(e)
        # return index(request)


# process logic
def process_logic(request, **kwargs):
    """
    process business logic
    :param request:
    :param kwargs:
    :return:
    """
    app = kwargs.get('app', None)
    path = kwargs.get('path', None)
    module = kwargs.get('module', None)
    try:
        fullPath = "%s.%s.%s" % (app, path, module)
        moduleObj = importlib.import_module(fullPath)
        funcObj = getattr(moduleObj, 'index')
        return funcObj(request)
    except (ImportError, AttributeError) as e:
        print (e)
        return HttpResponseNotFound()
    except Exception as e:
        print (e)
        return index(request)
