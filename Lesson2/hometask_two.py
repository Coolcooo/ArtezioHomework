"""Решение мини - заданий второй домашней работы"""


def task_one(segment):
    """Выводит квадраты нечетных чисел в отрезке
    от 0 до segment и их количество"""
    print("Задание №1")
    count = (segment - 1) // 2 + 1
    print(f"Квадраты нечетных чисел в интервале[0,{segment}]")
    for i in range(1, segment + 1, 2):
        print(i*i, end=" ")
    print()
    print(f"Количество нечетных чисел в интервале[0,{segment}]")
    print(count)


def task_two(first_interval, second_interval, denominator):
    """Вовращает количество чисел, делящихся на denominator,
    внутри заданного интервала"""
    print("Задание №2")
    count = 0
    for i in range(first_interval + 1, second_interval):
        if i == 0:
            continue
        if i % denominator == 0:
            count += 1
    return count


def task_three(factorial):
    """Возвращает факториал числа"""
    print("Задание №3")
    factor = 1
    for i in range(1, factorial + 1):
        factor = factor*i
    return factor


def task_four(start_or_stop, stop=0, step=1):
    """Имплементация функции range() из python 2.x"""
    print("Задание №4")
    range_python2 = []
    if stop == 0 and step == 1:
        i = 0
        while i < start_or_stop:
            range_python2.append(i)
            i += step
        return range_python2
    i = start_or_stop
    while i < stop:
        range_python2.append(i)
        i += step
    return range_python2


def task_five(password):
    """Проверяет введенный пользователем пароль с тем,
    что передан в функцию аргументом"""
    print("Задание №5")
    input_user = [
        input("Введите имя пользователя: "),
        input("Введите пароль: ")
    ]
    while input_user[1] != password:
        print(f"Password for user: <{input_user[0]}> is incorrect")
        print("Please try again...")
        input_user[1] = input("Введите пароль: ")
    print(f"Password for user: <{input_user[0]}> is correct")


task_one(5)
print(task_two(-1, 14, 7))
print(task_three(4))
print(task_four(2, 5, 2))
print(task_four(2, 5))
print(task_four(5))
task_five("Пароль")
