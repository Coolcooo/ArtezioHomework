"""Модуль для выполнения запроса к сайту"""
import requests


def request(input_url):
    """Функция для выполнения запроса и получения объекта
    (или None, в случае ошибки)"""
    try:
        return requests.get(input_url, timeout=2)
    except requests.exceptions.RequestException:
        return None
