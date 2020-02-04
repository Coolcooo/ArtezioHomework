"""Модуль функций для первой домашней работы"""


def task_one(original_row):
    """Возвращает строку, где каждое слово, если это возможно,
    начинается с заглавной буквы """
    print("Задание №1")
    list_str = original_row.split()
    for i, stroke in enumerate(list_str):
        if stroke[0].islower():
            list_str[i] = stroke[0].upper() + stroke[1:]
    return ' '.join(list_str)


def task_two(original_row):
    """Подсчитывает количество каждого символа в слове"""
    print("Задание №2")
    count_unique_characters = {}
    for i in original_row:
        count_unique_characters.update({i: original_row.count(i)})
    return count_unique_characters


def task_three(original_row):
    """Функция возвращает строку из 2- ух первых и 2 -ух последних
     символов,или пустую строку, если входная
     имеет меньше 2 - ух символов"""
    print("Задание №3")
    if len(original_row) < 2:
        return ''
    return original_row[:2] + original_row[-2:]


def task_four(original_row):
    """Функция возвращает количество строк в списке,
    где их длина больше 1, и первый и последний символ строки равны"""
    print("Задание №4")
    count = 0
    for i in original_row:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count


def task_five(first_set, second_set, third_set):
    """Функция проверяет, есть ли пересечение
     и у 1 - го, и у 2 - го множества с 3 - им"""
    print("Задание №5")
    return first_set.issuperset(third_set) and second_set.issuperset(third_set)


def task_six(max_key_dict):
    """Возвращает словарь c ключами от 1 до n,
    где у каждого элемента значение является квадратом ключа"""
    print("Задание №6")
    return{val_dict: val_dict*val_dict for val_dict
           in range(1, max_key_dict + 1)}


def task_seven(first_dict, second_dict):
    """Функция возвращает словарь,
    являющийся объединением двух словарей"""
    print("Задание №7")
    copy_first_dict = first_dict.copy()
    copy_first_dict.update(second_dict)
    return copy_first_dict


def task_eight(first_dict):
    """Функция возвращает три наибольших значения словаря"""
    print("Задание №8")
    sort_values_dict = list(first_dict.values())
    sort_values_dict.sort()
    return [sort_values_dict[-3], sort_values_dict[-2], sort_values_dict[-1]]


def task_nine(list_with_repeat):
    """Функция возвращает list без повторений"""
    print("Задание №9")
    list_without_repeat = list(set(list_with_repeat))
    return list_without_repeat


def task_ten(first_dict, second_dict):
    """Функция возвращает различия между двумя словарями"""
    print("Задание №10")
    update_dict = set(first_dict)
    update_dict.update(set(second_dict))
    return list(update_dict - set(first_dict).intersection(set(second_dict)))


STR_CHECK = "Привезенов владимир sergeevich 123фис"
print(task_one(STR_CHECK))

STR_CHECK = "google.com"
print(task_two(STR_CHECK))

STR_CHECK = "w3resource"
print(task_three(STR_CHECK))

LIST_CHECK = ["abc", "aba", "1221", "asc"]
print(task_four(LIST_CHECK))

SET_CHECK = ({1, 2}, {2, 3}, {2})
print(task_five(SET_CHECK[0], SET_CHECK[1], SET_CHECK[2]))

SET_CHECK = ({1, 2}, {3, 4}, {5})
print(task_five(SET_CHECK[0], SET_CHECK[1], SET_CHECK[2]))

VALUE = 5
print(task_six(VALUE))

DICT_CHECK = ({1: 3, 2: 1, 4: 2}, {1: 5, 2: 2})
print(task_seven(DICT_CHECK[0], DICT_CHECK[1]))

DICT_CHECK = {1: 2, 2: 2, 3: 3, 4: 4, 0: 5, 6: 6, 5: 7}
print(task_eight(DICT_CHECK))

LIST_CHECK = [1, 2, 3, 3, 4, 2, 1]
print(task_nine(LIST_CHECK))

LIST_CHECK = ([1, 2, 4, 6], [1, 2, 3])
print(task_ten(LIST_CHECK[0], LIST_CHECK[1]))
