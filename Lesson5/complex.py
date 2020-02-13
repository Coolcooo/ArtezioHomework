"""Модуль с реализацией класса Complex
и проверкой его работоспособности.
"""


class Complex(object):
    """Класс для работы с комплексными числами."""
    def __init__(self, a):
        self.real = float(a.split(' ')[0])
        self.imag = float(a.split(' ')[1])

    def __add__(self, other):
        return_ob = Complex('0 0')
        return_ob.real = self.real + other.real
        return_ob.imag = self.imag + other.imag
        return return_ob

    def __sub__(self, other):
        return_ob = Complex('0 0')
        return_ob.real = self.real - other.real
        return_ob.imag = self.imag - other.imag
        return return_ob

    def __mul__(self, other):
        return_ob = Complex('0 0')
        return_ob.real = self.real*other.real - self.imag*other.imag
        return_ob.imag = self.real*other.imag + self.imag*other.real
        return return_ob

    def __truediv__(self, other):
        return_obj = Complex('0 0')
        divider = other.real**2 + other.imag**2
        return_obj.real = (self.real*other.real + self.imag*other.imag) / divider
        return_obj.imag = (other.real*self.imag - self.real*other.imag) / divider
        return return_obj

    def __abs__(self):
        return_obj = Complex('0 0')
        return_obj.real = (self.real**2 + self.imag**2) ** 0.5
        return_obj.imag = 0
        return return_obj

    def __str__(self):
        if self.imag < 0:
            return '{}{}i'.format("{:.2f}".format(self.real),
                                  "{:.2f}".format(self.imag))
        return '{}+{}i'.format("{:.2f}".format(self.real),
                               "{:.2f}".format(self.imag))


C = Complex('2 1')
D = Complex('5 6')
print(C + D)
print(C - D)
print(C * D)
print(C/D)
print(abs(C))
print(abs(D))
