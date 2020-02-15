"""Модуль для создания и проверки функции - генератора chain."""


def chain(*iterables):
    """
    функция-генератор, которая последовательно
    итерирует переданные объекты.
    """
    for arg in iterables:
        for k in arg:
            yield k


GEN = chain('ABC', 'DEF')
for i in GEN:
    print(i)
