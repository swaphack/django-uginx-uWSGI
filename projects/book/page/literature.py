# -*- coding:utf-8 -*-

from foundation.control import ViewPage
from foundation.tools import get_label_text, get_params, create_html_node, create_html_template, load_file_content
from book.models import Book
import os


def get_navigation():
    navigation = create_html_node('navigation')

    template_url = 'framework/node/template-node-a-url-span-text.html'
    header_url = [
        {'url': '/', 'span': 'glyphicon glyphicon-home', 'text': 'ui_home'},
        {'url': 'book', 'span': 'glyphicon glyphicon-book', 'text': 'ui_book', 'active': '1'},
        {'url': 'audio', 'span': 'glyphicon glyphicon-headphones', 'text': 'ui_audio'},
        {'url': 'video', 'span': 'glyphicon glyphicon-film', 'text': 'ui_video'},
        {'url': 'account', 'span': 'glyphicon glyphicon-user', 'text': 'ui_account'},
    ]

    for item in header_url:
        node = create_html_template(template_url)
        for k in item:
            if k == 'text':
                node.set_attr(k, get_label_text(item[k]))
            else:
                node.set_attr(k, item[k])

        navigation.add_child(node)

    return navigation


def get_book_breadcrumb(book_id, chapter_id):
    books = Book.objects.filter(id=book_id)
    if books is None or len(books) == 0:
        return
    book = books[0]

    template_url = "framework/template-breadcrumb.html"
    item_url = [
        {'url': 'book/index?id=book_chapter&book=%s' % book_id, 'text': book.name},
        {'active': '1', 'text': chapter_id},
    ]

    breadcrumb = create_html_node('breadcrumb')

    for item in item_url:
        node = create_html_template(template_url)
        for k in item:
            node.set_attr(k, item[k])
        breadcrumb.add_child(node)

    return breadcrumb


def get_book_catalog(book_id):
    books = Book.objects.filter(id=book_id)
    if books is None or len(books) == 0:
        return
    book = books[0]

    catalog = create_html_node('catalog')
    for top, dirs, files in os.walk('static/book/%s' % book.book_dir):
        for file in files:
            item = create_html_template("")
            item.set_attr('text', file)
            item.set_attr('url', 'book/index?id=book_chapter_content&book=%s&chapter=%s' % (book_id, file))
            catalog.add_child(item)

    return catalog


def get_book_content(book_id, chapter_id):
    books = Book.objects.filter(id=book_id)
    if books is None or len(books) == 0:
        return
    book = books[0]

    content = load_file_content('static/book/%s/%s' % (book.book_dir, chapter_id))
    if content is None:
        return

    # content = content.replace(' ', '\t')

    chapter = create_html_node('chapter')
    chapter.set_attr('title', 'Technology')
    chapter.set_attr('body', content)
    return chapter


class BookChapterList(ViewPage):
    """
    章节列表
    """
    template_name = 'book/book_catalog.html'

    @classmethod
    def init_context(cls, request, context):
        params = get_params(request)

        book_id = params.get('book')

        context.get_header().add_child(get_navigation())
        context.get_content().add_child(get_book_catalog(book_id))

class BookChapterContent(ViewPage):
    """
    章节内容
    """
    template_name = 'book/book_chapter_content.html'

    @classmethod
    def init_context(cls, request, context):
        params = get_params(request)

        book_id = params.get('book')
        chapter_id = params.get('chapter')

        context.get_header().add_child(get_navigation())
        context.get_content().add_child(get_book_breadcrumb(book_id, chapter_id))
        context.get_content().add_child(get_book_content(book_id, chapter_id))
