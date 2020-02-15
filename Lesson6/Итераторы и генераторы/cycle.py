"""Модуль для создания и проверки функции - генератора cycle."""


def cycle(iterable):
    """функция-генератор cycle которая возвращает циклический итератор."""
    while iterable:
        for i in iterable:
            yield i


CHECK_LIST = [1, 2, 3]
GEN = cycle(CHECK_LIST)
print(next(GEN))
print(next(GEN))
print(next(GEN))
print(next(GEN))
print(next(GEN))
print(next(GEN))
print(next(GEN))
