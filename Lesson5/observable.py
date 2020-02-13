"""Модуль с классом Observable и проверкой наследования
от него и его работоспособности.
"""


class Observable(object):
    """Класс, получающий аттрибуты из kwargs,
    """
    def __init__(self, **kwargs):
        self._s = kwargs

    def __getattr__(self, item):
        try:
            return self._s[item]
        except KeyError:
            raise AttributeError

    def __dir__(self):
        attr_list = []
        for i in self._s:
            attr_list.append(i)
        return attr_list

    def __str__(self):
        k = f"{self.__class__.__name__}("
        for attr in dir(self):
            if attr[0] == '_':
                continue
            k += f"{attr}={self._s[attr]}, "
        if k[-1] == '(':
            return k + ')'
        return k[:-2] + ')'


class CheckClass(Observable):
    """Класс, созданный для проверки наследования от Observable"""


CHECK = CheckClass(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
print(CHECK)
print(CHECK.foo)
print(CHECK.name)
print(CHECK._bazz)
