"""
Модуль с декоратором, выполняющим каррирование функции,
и выполняющий его проверку.
 """

from inspect import signature


def curry(function):
    """Декоратор, выполняющий каррирование функции"""
    number_of_arguments = len(signature(function).parameters)

    def inner_decorator(recursion_count, args):
        def actual_inner_decorator(arg):
            if recursion_count <= 1:
                return function(*args, arg)
            args.append(arg)
            return inner_decorator(recursion_count - 1, args)

        return actual_inner_decorator

    return inner_decorator(number_of_arguments, [])


@curry
def sum_two_args(arg1: int, arg2: int):
    """Функция вычисляет сумму двух аргументов."""
    return arg1 + arg2


SUM1 = sum_two_args(1)
print(SUM1(5))
print(SUM1(7))
