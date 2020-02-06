"""Основной модуль программы, где происходит проверка на
работоспособность сайта, заданного пользователем"""

import website_alive.check_response as cr
INPUT_URL = input("Какой сайт хотите проверить? "
                  "(Запрос начинается на 'http://'): ")

if cr.check(INPUT_URL):
    print("Сайт работает исправно")
else:
    print("Хмм, что - то не так, попробуйте позже, "
          "либо проверьте правильность введенных данных.")
