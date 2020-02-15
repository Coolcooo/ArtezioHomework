"""Модуль с созданыым итератором и проверкой его работоспособности"""


class EvenIterator(object):
    """
    Итератор, который позволяет получить элементы списка на четных позициях.
    """
    def __init__(self, source_list):
        self.source_list = source_list
        self.counter = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 2
        if self.counter < len(self.source_list):
            return self.source_list[self.counter]
        raise StopIteration


CHECK_LIST = [0, 1, 2, 3, 4, 5]
IT = EvenIterator(CHECK_LIST)
print(list(IT))
