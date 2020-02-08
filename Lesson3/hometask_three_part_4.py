"""Модуль предназначен для тестирования функции разбиения xml документа"""
import xml.etree.cElementTree as eT


def xml_to_dict_and_max_depth(xml_string):
    """Функция делает из строки с xml - документом дерево - словарь
    и показывает максимальную глубину.
    """
    root = eT.fromstring(xml_string)
    dict_tree = {"name": root.tag, "children": list(root)}
    depth = 0

    def add_children(parent):
        nonlocal depth
        uniqueness_check = True
        for i, children in enumerate(parent["children"]):
            if uniqueness_check:
                depth += 1
                uniqueness_check = False
            parent["children"][i] = {"name": children.tag,
                                     "children": list(children)}
            add_children(parent["children"][i])
    add_children(dict_tree)

    return dict_tree, depth


CHECK_XML_STRING = "<root><element1 /><element2 /><element8 />" \
                   "<element3><element4><element5 /><element6><element20 />" \
                   "</element6></element4></element3></root>"
print(xml_to_dict_and_max_depth(CHECK_XML_STRING))

CHECK_XML_STRING = "<root><element1 /><element2 />" \
                   "<element3><element4 /></element3></root>"
print(xml_to_dict_and_max_depth(CHECK_XML_STRING))
