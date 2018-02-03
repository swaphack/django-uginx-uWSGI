#!/usr/bin/env python
import os
from resources.models import Resource
from django.shortcuts import HttpResponse

from foundation.control import LogicEvent
from foundation.factory import Singleton
from projects.settings import BASE_DIR
import thread


def traversal_dir(top, func):
    if func is None:
        return
    for root, dirs, files in os.walk(top):
        for file in files:
            func('%s/%s' % (root, file))


def update_image_data(root, full_path):
    filename = os.path.basename(full_path)
    name = os.path.splitext(filename)[0]
    path = full_path[len(root):]
    path = path.replace('\\', '/')

    result = Resource.objects.filter(name=name)
    if result is None or len(result) == 0:
        Resource.objects.create(name=name, path=path)
    else:
        result.update(path=path)


def copy_app_images_to_db(root, dir_name):
    image_root = os.path.join(root, dir_name)
    traversal_dir(image_root, lambda full_path: update_image_data(root, full_path))


class ResDB(LogicEvent, Singleton):
    def __init__(self):
        LogicEvent.__init__(self)

        self.bind('load_db', self.load_db)

    def load_db(self, request, params):
        root = os.path.join(BASE_DIR, 'static')

        thread.start_new_thread(copy_app_images_to_db, (root, 'images'))

        return HttpResponse("Start")

