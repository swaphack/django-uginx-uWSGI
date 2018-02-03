# -*- coding: utf-8 -*-

from foundation.factory import Singleton
from resources.models import Text, Resource
from resources.data.language import LanguageManager


class TextManager(Singleton):

    def __init__(self):
        Singleton.__init__(self)

    def get_text(self, name):
        data = Text.objects.filter(name=name)
        if data is None:
            return ""
        elif len(data) == 0:
            return ""
        else:
            cell = data[0]
            lang_text = LanguageManager.singleton().get_lang_text()
            text = getattr(cell, lang_text, "")
            return text


class ResourceManager(Singleton):
    def __init__(self):
        Singleton.__init__(self)

    def get_path(self, name):
        data = Resource.objects.filter(name=name)
        if data is None:
            return ""
        elif len(data) == 0:
            return ""
        else:
            cell = data[0]
            return cell.path


