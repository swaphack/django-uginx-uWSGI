# -*- coding:utf-8 -*-

from dataset import Dictionary, List

class HTMLNode:
    """
    html node, contain marks and children
    """
    def __init__(self):
        self.__name = "item"
        self.__id = ""
        self.__attr = Dictionary()
        self.__children = List()

    def set_id(self, val):
        self.__id = val
        return self

    def get_id(self):
        return self.__id

    def set_name(self, val):
        self.__name = val
        return self

    def get_name(self):
        return self.__name

    def set_attr(self, key, val):
        self.__attr.set(key, val)
        return self

    def get_attr(self, key):
        return self.__attr.get(key)

    def remove_all_attrs(self):
        self.__attr.clear()

    def add_child(self, node):
        self.__children.add(node)
        return self

    def remove_child(self, node):
        self.__children.remove(node)
        return self

    def remove_all_children(self):
        self.__children.clear()

    def data(self):
        child_data = []
        data = self.__children.data()
        for child in data:
            if isinstance(child, HTMLNode):
                child_data.append(child.data())

        dom = {'name': self.get_name(), 'id': self.get_id(), 'children': child_data}
        dom.update(self.__attr.data())
        return dom

    def html(self):
        node = []
        node.append('<')
        node.append(self.get_name())
        node.append(' ')

        attrs = self.__attr.data()
        for (k, v) in attrs:
            node.append(k)
            node.append('=')
            node.append(v)
            node.append(' ')

        node.append('>')

        children = self.__children.data()
        for v in children:
            node.append(v.html())

        node.append('</')
        node.append(self.get_name())
        node.append('>')

        return ''.join(node)


class HTMLTemplate(HTMLNode):
    """
    define a template moduel, and render it with data
    """
    def __init__(self):
        HTMLNode.__init__(self)
        self.__template = ""

    def set_template(self, temp):
        self.__template = temp

    def get_template(self):
        return self.__template

    def data(self):
        dom = {'node': self.get_template()}
        data = HTMLNode.data(self)
        dom.update(data)
        return dom

