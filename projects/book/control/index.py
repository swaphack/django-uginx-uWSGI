# -*- coding: utf-8 -*-

from foundation.control import LogicEvent
from foundation.dataset import Dictionary

from book.page.index import MainPage
from book.page.literature import BookChapterContent, BookChapterList


class BookLogic(LogicEvent):
    def __init__(self):
        LogicEvent.__init__(self)

    def index(self, request):
        return MainPage.flush(request)

    @staticmethod
    def book_chapter(request, params):
        if not isinstance(params, Dictionary):
            raise Exception
        if not params.has('book'):
            raise Exception

        return BookChapterList.flush(request)

    @staticmethod
    def book_chapter_content(request, params):
        if not isinstance(params, Dictionary):
            raise Exception
        if not params.has('book', 'chapter'):
            raise Exception

        return BookChapterContent.flush(request)


def index(request):
    return BookLogic.dispatch('id', request)


