import test46
import json
from io import StringIO

# Кодирование данных в формат JSON выполняет функция dumps() | выдает данные в виде строки

test_data = [1, 2, 4, "di", ["3"], {"dict": 34}]
test_data_2 = {"job": "Разработка сайтов", "price": 20000,
        "platforms": ("Python", "MySQL", "Apache")}

# Кодируем список
test_json = json.dumps(test_data)
# Кодируем словарь
test_json_2 = json.dumps(test_data_2)

print(test_json)
print(test_json_2) # Кириллица => {"job": "\u0420\u0430\..."}

# dump() - записывает результат в файло­вый объект

sio = StringIO()

json.dump(test_data_2, sio, ensure_ascii=False)

s_json = sio.getvalue()

print(s_json) # {"job": "Разработка сайтов", ...}

sio.close()

# loads() - Для декодирования данных JSON, из модуля json.

s1 = '{"job": "Разработка сайтов", "price": 20000,'
s1 += '"platforms": ["Python", "MySQL", "Apache"]}'

# Декорируем словарь
print(json.loads(s1))

# Преобразуем все целые числа в вещественные
print(json.loads(s1, parse_int=float))

