import test46
from xml.sax.saxutils import escape, quoteattr, unescape
from urllib.parse import urlencode
import html
from http.client import HTTPConnection

# Разбор HTML-эквивалентов

# ♦ escape(<Строка>[,<Словарь>]) — заменяет символы <, > и & соответствующими HTML-эквивалентами

s = """ &<>" """
print(escape(s)) # & ~ &amp, < ~ &lt, > ~ &gt, " вывод: &amp;&lt;&gt;"

# ♦ quoteattr(<Строка>[, <Словарь>]) - Аналогична escape разве что добавляет кавычки

print(quoteattr(s)) # Вывод: ' &amp;&lt;&gt;" '

# ♦ unescape (<Строка>[, <Словарь>]) — заменяет HTML-эквиваленты обычными символами

s_1 = escape(s)
print(unescape(s_1)) # Вывод: &<>"

print(html.escape(s)) # Вывод: &amp;&lt;&gt;&quot; 

# Обмен данными по протоколу HTTP

# ♦ Модуль http.client позволяет получить информацию из Интернета по протоколам HTTP и HTTPS.
# Отправить запрос можно методами GET, POST и HEAD.

# Для создания объекта соединения, использующего протокол HTTP, предназначен класс HTTPConnection
# HTTPConnection(<Домен>[,<Порт>[,timeout[,source_address=None]]])

con = HTTPConnection("test1.ru")

# После создания объекта соединения необходимо отправить запрос, вызвав метод request ()
# request(<Метод>,<Путь>[,body=None][,headers=<Заголовки>])

# getresponse() - возвращает результат выполненного запроса, представленный в виде объекта класса

# Прочитать ответ сервера можно с помощью метода read( [количество байт>]) класса HTTPResponse.
# Метод read() возвращает последовательность байтов, а не строку.
# Закрыть объект соединения позволяет метод close ()

data = urlencode({"color": "Красный", "var": 15}, encoding="UTF-8")
headers = {"User-Agent": "MySpider/1.0",
"Accept": "text/html, text/plain, application/xml",
"Accept-Language": "ru, ru-RU",
"Accept-Charset": "UTF-8",
"Content-Type": "application/x-www-form-urlencoded",
"Referer": "/index.php" }
con = HTTPConnection("localhost")
try:
    con.request("POST", "/testrobots.php", data, headers=headers)
    result = con.getresponse() # Создаем объект результата
    print(result.read().decode("UTF-8"))
except:
    print("error")