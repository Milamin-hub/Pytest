import test46
from urllib.parse import urlparse, quote_from_bytes, unquote
from urllib.parse import urljoin

# URL-адрес coстоит из- <Протокол>://<Домен>:<Порт>/<Путь>;<Параметры>?<Запрос>#<Якорь>

# Схема URL-адреса для протокола FTP выглядит- <Протокол>://<Пользователь>:<Пароль>@<Домен>

# urlparse() - Позволяет разобрать URL-адрес на составляющие
# urlparse(<URL-адрес>[,<Схема>[,<Разбор якоря>]])
# Объект можно преобразовать в кортеж из следующих элементов:
#  (scheme, netloc, path, params, query, fragment) 
# => <scheme>://<netloc>/<path>;<params>?<query>#<fragment>.

url = urlparse("https://animevost.org/tip/tv/2642-tantei-wa-mou-shindeiru.html")
print("%s" % url.scheme + "://" + "%s" % url.netloc + "%s" % url.path)

code_b = quote_from_bytes(bytes("Пилить не чилить", encoding="UTF-8"))
print(code_b)
encode_b = unquote("%s" % code_b, encoding="UTF-8")
print(encode_b)

# urljoin() - Преобразовывает относительную ссылку в абсолютный URL-адрес

test_h = urljoin('https://animevost.org/tip/tv/2642-tantei-wa-mou-shindeiru.html' , './2642-tantei-wa-mou-shindeiru.html')
print(test_h)