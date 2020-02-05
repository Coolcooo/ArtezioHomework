"""Модуль для решения второй задачи третьего домашнего задания,
 где требуется вичислить сумму и произведение всех чисел
 (даже вложенных в другие списки и кортежи) в списке или кортеже"""


def task_one(*args, set_id=None):
    """Функция возвращает сумму и произведение всех чисел внутри списка
     или кортежа, либо None, если передана циклическая ссылка"""
    if set_id is None:
        set_id = set()
        set_id.add(id(args))
    total = 0
    composition = 1
    for i in args:
        if isinstance(i, (float, int)):
            if i != 0:
                total += i
                composition *= i
        else:
            if id(i) in set_id:
                print("В качестве аргумента передана циклическая ссылка")
                return None
            set_id.add(id(i))
            recursion = task_one(*i, set_id=set_id)
            if recursion is None:
                return None
            total += recursion[0]
            composition *= recursion[1]
    return [total, composition]


FIRST_LIST = [1, 2, 3]
SECOND_LIST = [1, 2, 4]
THIRD_LIST = [1, 2, [3, 4, (5, 6, 2, [1, 2, (5, 4, 0)])], 2, [3, 0]]

print(task_one(THIRD_LIST))
print()

FIRST_LIST.append(SECOND_LIST)
SECOND_LIST.append(THIRD_LIST)
THIRD_LIST.append(FIRST_LIST)
print(task_one(FIRST_LIST))
