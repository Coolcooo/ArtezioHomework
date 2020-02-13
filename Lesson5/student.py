"""Модуль с реализацией класса Student и проверкой его методов"""


class Student(object):
    """Класс хранит информацию об обучаемом на курсе"""
    _NUMBER_OF_ATTEMPTS = 2

    def __init__(self, a, b):
        self.name = a
        self._info = b
        self._uncompleted_lab = list(range(self._info["lab_num"]))
        self.points = {i: 0 for i in range(self._info["lab_num"])}
        self.points["exam"] = 0
        self.attempt = {i: 0 for i in range(self._info["lab_num"])}
        self.attempt["exam"] = False

    def make_lab(self, number_of_points, lab_number=None):
        """Функция проставляет баллы за лабораторные работы."""
        if number_of_points > self._info["lab_max"]:
            number_of_points = self._info["lab_max"]
        if number_of_points < 0:
            return self
        if len(self._uncompleted_lab) == 0:
            lab_number = int(input("Введите номер лабораторной работы: "))
        if lab_number is None:
            self.points[self._uncompleted_lab[0]] = number_of_points
            self.attempt[self._uncompleted_lab.pop(0)] += 1
            return self
        try:
            if self.attempt[lab_number] < self._NUMBER_OF_ATTEMPTS:
                self.attempt[lab_number] += 1
        except KeyError:
            self.attempt[lab_number] = 0
        if self.attempt[lab_number] < self._NUMBER_OF_ATTEMPTS:
            self.points[lab_number] = number_of_points
        else:
            print(f"Работа №{lab_number} не засчитана"
                  " - все попытки использованы")
        return self

    def make_exam(self, exam_grade):
        """Функция проставляет баллы за экзамен."""
        if self.attempt["exam"]:
            print("Повторная сдача экзамена невозможна")
            return self
        if exam_grade > self._info["exam_max"]:
            exam_grade = self._info["exam_max"]
        if exam_grade < 0:
            return self
        self.points["exam"] = exam_grade
        self.attempt["exam"] = True
        return self

    def is_certified(self):
        """Функция проверяет, достаточно ли баллов для сертификата."""
        pass_score = self._info["k"] * (self._info["exam_max"] +
                                        self._info["lab_max"] *
                                        self._info["lab_num"])
        pas = self.points["exam"]
        for i in range(self._info["lab_num"]):
            pas += self.points[i]
        return pas >= pass_score

    def __str__(self):
        if self.is_certified():
            return f"{self.name}{self.points} - Сертифицирован"
        return f"{self.name}{self.points} - Не сертифицирован"


CONF = {"exam_max": 30, "lab_max": 7, "lab_num": 10, "k": 0.61}
VLADIMIR = Student("Владимир", CONF)
VLADIMIR.make_lab(1)
VLADIMIR.make_lab(1)
VLADIMIR.make_lab(1)
VLADIMIR.make_lab(1)
VLADIMIR.make_lab(1)
VLADIMIR.make_lab(1)
VLADIMIR.make_lab(1)
VLADIMIR.make_lab(8)
VLADIMIR.make_lab(20, 5)
VLADIMIR.make_lab(8, 5)
VLADIMIR.make_lab(8, 5)
VLADIMIR.make_lab(8, 5)
VLADIMIR.make_lab(8, 5)
VLADIMIR.make_lab(7, 20)
VLADIMIR.make_lab(7, 20)
VLADIMIR.make_lab(7, 20)
VLADIMIR.make_exam(25)
VLADIMIR.make_exam(35)

print(VLADIMIR)
