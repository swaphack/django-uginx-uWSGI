# -*- coding:utf-8 -*-
import os

from projects.settings import BASE_DIR
from foundation.dataset import Dictionary, List
from foundation.html import HTMLNode, HTMLTemplate

from resources.data.resource import TextManager, ResourceManager


def auto_import_models(appname, dir):
    root = os.path.join(BASE_DIR, appname)
    root = os.path.join(root, dir)
    lst = os.listdir(root)
    for i in range(0, len(lst)):
        if lst[i].endswith('.py'):
            name = lst[i][:-3]
            if name == "__init__":
                continue
            else:
                tbl = 'from %s.tables.%s import *' % (appname, name)
                try:
                    exec ( tbl )
                except Exception as e:
                    continue


def load_file_content(filename):
    fullpath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(fullpath):
        return None

    fd = open(fullpath, "rb")
    if fd is None:
        return None

    content = fd.read()
    fd.close()

    return content


def create_dict(**kwargs):
    return Dictionary(**kwargs)


def create_list(*args):
    return List(*args)


def get_label_text(name):
    return TextManager.singleton().get_text(name)


def get_res_path(name):
    return ResourceManager.singleton().get_path(name)


def create_html_node(name):
    node = HTMLNode()
    node.set_name(name)
    return node

def get_params(request):
    """
    :param request:
    :return:
    """
    params = {}
    """
    if request.method == "POST":
        params = request.POST
    elif request.method == "GET":
        params = request.GET
    """
    for k in request.GET:
        params[k] = request.GET[k]

    for k in request.POST:
        params[k] = request.POST[k]

    return params


def create_html_template(template_url):
    node = HTMLTemplate()
    node.set_template(template_url)
    return node


