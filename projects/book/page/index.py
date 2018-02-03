# -*- coding:utf-8 -*-

from foundation.control import ViewPage

from foundation.tools import get_label_text, create_html_node, create_html_template


def get_navigation():
    navigation = create_html_node('navigation')

    template_url = 'framework/node/template-node-a-url-span-text.html'
    header_url = [
        {'url': '/', 'span': 'glyphicon glyphicon-home', 'text': 'ui_home'},
        {'url': 'book', 'span': 'glyphicon glyphicon-book', 'text': 'ui_book'},
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

class MainPage(ViewPage):
    template_name = 'book/index.html'

    @classmethod
    def init_context(cls, request, context):
        context.get_header().add_child(get_navigation())
