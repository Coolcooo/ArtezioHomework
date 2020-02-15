"""
Модуль, где словарь генерируется из двух списков, первый
отвечает за ключи, а второй за значения.
"""

KEYS = [1, 2, 3]
VALUES = ['one', 'two']
DICT = {KEYS[i]: VALUES[i] if i < len(VALUES) else None for i in range(len(KEYS))}
print(DICT)
