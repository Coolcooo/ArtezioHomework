"""Модуль с шаблоном регулярных выражений для поиска даты и времени"""


import re

MESSAGE1 = '2020-10-12T18:25+03:00sfds'
MESSAGE2 = '2020-10-12T18:25-03:00sfds'
PATTERN = r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})(\+|-)(\d{2}):(\d{2})'
SEARCH1 = re.search(PATTERN, MESSAGE1)
SEARCH2 = re.search(PATTERN, MESSAGE2)
print(SEARCH1.group())
print(SEARCH2.group())
