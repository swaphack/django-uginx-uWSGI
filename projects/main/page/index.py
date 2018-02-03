# -*- coding: utf-8 -*-

from resources.data.resource import TextManager, ResourceManager
from foundation.tools import create_html_node, create_html_template
from foundation.control import ViewPage


def get_navigation():
    template_url = 'framework/node/template-node-a-url-span-text.html'
    header_url = [
        {'url': '/', 'span': 'glyphicon glyphicon-home', 'text': 'ui_home', 'active': '1'},
        {'url': 'book', 'span': 'glyphicon glyphicon-book', 'text': 'ui_book'},
        {'url': 'audio', 'span': 'glyphicon glyphicon-headphones', 'text': 'ui_audio'},
        {'url': 'video', 'span': 'glyphicon glyphicon-film', 'text': 'ui_video'},
        {'url': 'account', 'span': 'glyphicon glyphicon-user', 'text': 'ui_account'},
    ]

    navigation = create_html_node('navigation')

    for item in header_url:
        node = create_html_template(template_url)
        for k in item:
            if k == 'text':
                node.set_attr(k, TextManager.singleton().get_text(item[k]))
            else:
                node.set_attr(k, item[k])

        navigation.add_child(node)

    return navigation


def get_carousel():
    template_url = 'framework/node/template-node-img-url-src.html'
    carousel_url = [
        {'url': '#', 'src': 'activity_icon102', 'active': '1'},
        {'url': '#', 'src': 'activity_icon103'},
        {'url': '#', 'src': 'activity_icon104'},
    ]

    carousel = create_html_node('carousel')
    carousel.set_id('carousel-images')

    for item in carousel_url:
        node = create_html_template(template_url)
        for k in item:
            if k == 'src':
                node.set_attr(k, ResourceManager.singleton().get_path(item[k]))
            else:
                node.set_attr(k, item[k])
        carousel.add_child(node)

    return carousel


class HomePage(ViewPage):
    template_name = "home/index.html"

    @classmethod
    def init_context(cls, request, context):
        context.get_header().add_child(get_navigation())
        context.get_content().add_child(get_carousel())
