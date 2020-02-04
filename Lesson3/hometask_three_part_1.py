"""Функции для задания №1 домашней работы №3"""


def task_one(input_list):
    """Функция возвращает список квадратов элементов
    списка или кортежа"""
    output_list = []
    for i in input_list:
        output_list.append(i * i)
    return output_list


def task_two(input_list):
    """Функция возвращает список элементов на четных позициях"""
    output_list = []
    for i in range(1, len(input_list), 2):
        output_list.append(input_list[i])
    return output_list


def task_three(input_list):
    """Функция возвращает список кубов четных элементов
    на нечетных позициях"""
    output_list = []
    for i in range(0, len(input_list), 2):
        if input_list[i] % 2 == 0:
            output_list.append(input_list[i] ** 3)
    return output_list


LIST_CHECK = [1, 2, 3, 4, 5, 7, 8]
print(task_one(LIST_CHECK))
print(task_two(LIST_CHECK))
print(task_three(LIST_CHECK))
