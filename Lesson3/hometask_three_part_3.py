"""Реализация 3 задания из 3-ей домашней работы"""

def fun1():
    """Функция возвращает список из среднего арифметического
    и максимального элемента за все время вызова функции"""
    max_element = None
    def fun2(first, second, third, fourth):
        nonlocal max_element
        if max_element is None:
            max_element = max(first, second, third, fourth)
        max_element = max(max_element, first, second, third, fourth)
        return (first + second + third + fourth) / 4, max_element

    return fun2


FIND_AVERAGE_AND_MAX = fun1()
print(FIND_AVERAGE_AND_MAX(2, 3, 4, 5))
print(FIND_AVERAGE_AND_MAX(2, 3, 4, 2))
print(FIND_AVERAGE_AND_MAX(2, 3, 7, 2))
print(FIND_AVERAGE_AND_MAX(2, 2, 2, 2))
