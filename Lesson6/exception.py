"""Модуль для проверки исключений при целочисленном делении"""

T = int(input())
for i in range(T):
    a = input().split()
    try:
        print(int(a[0]) // int(a[1]))
    except ZeroDivisionError as err:
        print("Error Code:", err)
    except ValueError as err:
        print("Error Code:", err)
