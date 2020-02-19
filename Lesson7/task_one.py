"""
Модуль с реализацией декоратора,который показывает
среднее время выполнения функции за n последних вызовов,
а так же проверкой этого декоратора на функциях.
"""


from time import time, sleep


def average_time(number_of_recent_calls):
    """
    Декоратор,который показывает среднее время выполнения функции
    за n последних вызовов.
     """
    def inner_decorator(function):
        total = 0
        count = 0
        recent_calls = []

        def wrapper(*args, **kwargs):
            nonlocal total, count

            start = time()
            result = function(*args, **kwargs)
            lead_time = round((time() - start) * 1000)
            if count == number_of_recent_calls:
                total -= recent_calls.pop(0)
                recent_calls.append(lead_time)
            else:
                recent_calls.append(lead_time)
                count += 1

            total += lead_time
            print(f"Среднее время работы: {total // count} мс")
            return result

        return wrapper

    return inner_decorator


@average_time(number_of_recent_calls=2)
def good_night(time_to_sleep):
    """Функция, которая просто спит."""
    sleep(time_to_sleep)
    return time_to_sleep


assert good_night(3) == 3
assert good_night(7) == 7
assert good_night(1) == 1
