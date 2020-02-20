"""
Модуль с декоратором, определяющим среднее время
избранных методов, и его проверкой.
"""


from time import time, sleep


def time_methods(*methods):
    """Декоратор, измеряющий время работы методов."""
    def class_wrapper(specific_class):
        getattribute = specific_class.__getattribute__

        def new_getattribute(instance, name):
            attr = getattribute(instance, name)
            if name in methods:
                def method_wrapper(*args, **kwargs):
                    start = time()
                    result = attr(*args, **kwargs)
                    print(f"Время работы метода {name}: {time() - start}")
                    return result

                return method_wrapper
            return attr

        specific_class.__getattribute__ = new_getattribute
        return specific_class

    return class_wrapper


@time_methods('inspect','foo')
class Spam:
    """Тестовый класс, созданный для проверки декоратора."""
    def __init__(self, arg):
        self.arg = arg

    def inspect(self):
        """Метод, заставляющий объект спать."""
        sleep(self.arg)

    def get_arg(self):
        """Метод - геттер аргумента."""
        return self.arg


SOME_CLASS = Spam(2)
SOME_CLASS.inspect()
print(SOME_CLASS.get_arg())
