"""
Модуль с функцией, позволяющей отправить изображение в виде запроса
на сервер, получить ответ в виде изображения,
раскодировать его, сохранить, и узнать его размер,
а так же с проверкой этой функции.
  """

from base64 import b64decode
from requests import post


def image_post(path, name_new_image):
    """
    Функция отправляет запрос на сервер с изображением,
    сохраняет полученное в ответе изображение и возвращает его размер.
     """
    url = "https://postman-echo.com/post"
    file_name_post = path.split('/')[-1]
    response = post(url, files={file_name_post: open(path, 'rb')}).json()
    decode = 'data:application/octet-stream;base64,'
    get_file = b64decode(response['files'][file_name_post][len(decode):])
    open(name_new_image, 'wb').write(get_file)
    return len(get_file)


print(image_post("./1.jpg", "newfile.jpg"))
