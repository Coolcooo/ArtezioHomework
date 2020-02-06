"""Модуль для проверки, получили ли мы ошибку
 или запрос был успешно обработан"""
import website_alive.make_request as req


def check(check_url):
    """модуль для проверки полученного запроса"""
    if req.request(check_url) is None:
        return False
    return req.request(check_url).status_code == 200
