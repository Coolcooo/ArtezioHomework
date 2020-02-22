"""Модуль включает функцию, с конвертером валют и ее проверку."""

from requests import get


def currency_transfer(value, current_currency, final_currency):
    """Функция - конвертер валют."""
    response = get("https://api.exchangerate-api.com/v4/latest/" +
                   current_currency).json()
    course = response['rates'][final_currency]
    return round(value * course, 2)


print(currency_transfer(700, 'RUB', 'USD'))
