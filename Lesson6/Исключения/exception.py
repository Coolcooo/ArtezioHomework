"""
Модуль, представляющий решение задачи по ссылке:
https://www.hackerrank.com/challenges/exceptions/problem
"""

NUMBER_OF_EXAMPLES = int(input())
for i in range(NUMBER_OF_EXAMPLES):
    a = input().split()
    try:
        print(int(a[0]) // int(a[1]))
    except ZeroDivisionError as err:
        print("Error Code:", err)
    except ValueError as err:
        print("Error Code:", err)
