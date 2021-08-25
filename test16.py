""" Работа со строками """

""" ♦ bytes — неизменяемая последовательность байтов """

str_1 = "Строка".encode(encoding = 'utf-8')
print("Последовательность байтов: ", str_1)

str_2 = len(bytes("Строка", encoding = 'utf-8'))
print("Количество байтов: ", str_2)

""" ♦ bytearray — изменяемая последовательность байтов """

s = bytearray("str", "cp1251")
str_3 = s[0] = 55
# str_3 = s.append(55) Добавляем символ
print("Количество байтов: ", str_3)

obj1, obj2 = bytes ("строка1", "utf-8"), bytearray("строка2", "utf-8")
print(obj1, obj2)
str_4 = str(obj1, "utf-8"), str(obj2, "utf-8")
print(str_4)

def test():
    """ Описание функции """
    pass

print(test.__doc__)

"""
Если перед строкой разместить модификатор "r", то специальные символы внутри строки
выводятся как есть 
"""


#♦ \n — перевод строки;
#♦ \r — возврат каретки;
#♦ \t — знак табуляции;
#♦ \v — вертикальная табуляция;
#♦ \a — звонок;
#♦ \b — забой;
#♦ \f — перевод формата;
#♦ \0 — нулевой символ (не является концом строки);
#♦ \" — кавычка;
#♦ \' — апостроф;
#♦ \N — символ с восьмеричным кодом N. Например, \74 соответствует символу <;
#♦ \xN — символ с шестнадцатеричным кодом N. Например, \x6a соответствует символу j;
#♦ \\ — обратный слэш;
#♦ \uxxxxx — 16-битный символ Unicode. Например, \u043a соответствует русской букве к;
#♦ \uxxxxxxxx — 32-битный символ Unicode.


print("Экспанируем слеш \\ явным образом")

s = "Python"

for i in range(len(s)): print(s[i], end=" ")
print()

for i in s: print(i, end=" ")
print()

print("Cтрока_1" + "\nСтрока_2")

print("PY" in "Python")

""" % ~ format()"""



print("%s-%s-%s" % (10, 20, 30)) # Форматирование

print("%(name)s - %(year)s" % {"name": "Nick", "year": 2001})

""" г — преобразует любой объект в строку с помощью функции герг() """

print("%r" % ("Обычная строка"))

""" а — преобразует объект в строку с помощью функции ascii() """

print("%a" % ("Обычная строка"))

""" с — выводит одиночный символ или преобразует числовое значение в символ """

for i in range(1, 21): print("%s => %c" % (i, i))

""" e — вещественное число в экспоненциальной форме (буква е в нижнем регистре) """

print("%e %e" % (3000, -34945.34))

print("{0} - {1} - {2}".format(10, 12.3, "string")) # Форматирование по индексу

""" join() — преобразует последовательность в строку """

print(" => ".join(["word1", "word2", "word3"]))