"""Модуль с функцией получения размера html - страницы и ее проверкой."""


from requests import get


def html_size(url):
    """Функция считает размер html - страницы."""
    return len(get(url).text)


print(html_size("http://google.com"))
