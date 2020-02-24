"""
Модуль с шаблоном регулярного выражения, который ищет вопросительные
предложения, включающие в себя слово длиннее двух символов
и повторяющееся больше 3 раз.
"""

import re

PATTERN = r"(?=[^!.?]*((?:(?<=[\s.!?])|(?<=^))[a-zA-Zа-яА-Я0-9]{3,}" \
          r"(?=[\s?.!]))(?:.*\s\1(?=[\s?])){3,})[^.?!]+\?"

MESSAGE = "how howhow h sdf how how are you?" \
          " Hello dfg Hello Hello Hello?" \
          " Как твои дела, как жизнь, как учеба, как на личном?"

MATCHES = re.finditer(PATTERN, MESSAGE, re.MULTILINE | re.IGNORECASE)

for matchNum, match in enumerate(MATCHES, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(
        matchNum=matchNum, start=match.start(), end=match.end(),
        match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(
            groupNum=groupNum, start=match.start(groupNum),
            end=match.end(groupNum), group=match.group(groupNum)))
