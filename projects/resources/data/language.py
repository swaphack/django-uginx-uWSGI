# -*- coding: utf-8 -*-

from foundation.factory import Singleton
from foundation.common import enum
from resources.models import Language

LANG_TYPE = enum('cn', 'en', 'arb')

class LanguageManager(Singleton):
    """
    projects language
    """
    def __init__(self):
        Singleton.__init__(self)
        self.__lang = LANG_TYPE.cn

    def set_lang(self, lang):
        self.__lang = lang

    def get_lang(self):
        return self.__lang

    def get_lang_text(self):
        data = Language.objects.filter(kind=self.get_lang())
        if data is None:
            return ""
        elif len(data) == 0:
            return ""
        else:
            cell = data[0]
            return cell.lang

    def get_lang_label(self):
        Language.objects.filter()
