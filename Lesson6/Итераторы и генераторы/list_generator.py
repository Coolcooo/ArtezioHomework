"""
Модуль, показывающий реализацию генератора
списка публичных аттрибутов объекта.
"""


class SomeClass(object):
    """Класс-образец с какими - то аттрибутами."""
    some_attr_1 = 0
    some_attr_2 = 2
    some_attr_3 = 5
    _some_attr_4 = 6


SOME_OBJECT = SomeClass()
PUBLIC_ATTR_LIST = [x for x in dir(SOME_OBJECT) if x[0] != '_']
print(PUBLIC_ATTR_LIST)
