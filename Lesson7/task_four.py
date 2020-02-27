"""
Модуль с декоратором, проверяющим аннотацию функции,
 а так же функцией - тестом.
"""

from inspect import signature


def check_annotation(function):
    """
    Декоратор, проверяющий аннотацию на полноту
    и соответствие аргументов ей.
    """
    if len(signature(function).parameters) > len(function.__annotations__):
        raise Warning

    def wrapper(*args, **kwargs):
        mapping_arguments = signature(function).bind(*args, **kwargs)
        mapping_arguments.apply_defaults()
        mapping_arguments = dict(mapping_arguments.arguments)
        annotation = function.__annotations__
        for i in annotation:
            if i == 'args':
                for j in mapping_arguments[i]:
                    if not isinstance(j, annotation[i]):
                        print(
                            f"Аргумент {j} в args не соответствует аннотации.")
            elif i == 'kwargs':
                for j in mapping_arguments[i].items():
                    if not isinstance(j[1], annotation[i]):
                        print(
                            f"Аргумент {j[0]} в kwargs не соответствует "
                            "аннотации.")
            else:
                if not isinstance(mapping_arguments[i], annotation[i]):
                    print(f"Аргумент {i} не соответствует аннотации.")

        return function(*args, **kwargs)

    return wrapper


@check_annotation
def sum_of_all_arguments(arg1: int, arg2: int, arg3: int, *args: int,
                         kwarg1: int = 7, **kwargs: int):
    """Функция - сумма всех аргументов с округлением до двух знаков."""
    sum_args_kwargs = 0
    for i in args:
        sum_args_kwargs += i
    for i in kwargs:
        sum_args_kwargs += kwargs[f'{i}']
    return round(sum_args_kwargs + arg1 + arg2 + arg3 + kwarg1, 2)


print(sum_of_all_arguments(1.2, 1.2, 1.3, 1, 2, 1.5, 1.6, 1.7, k=5, kwarg1=3.2,
                           v=8.6))
