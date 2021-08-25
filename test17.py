import locale

""" module locale """
""" setlocal() - служит для установки настроек в module locale """
""" 
♦ locale.LC_ALL — устанавливает локаль для всех режимов;
♦ locale.LC_COLLATE — для сравнения строк;
♦ locale.LC_CTYPE — для перевода символов в нижний или верхний регистр;
♦ locale.LC_MONETARY — для отображения денежных единиц;
♦ locale.LC_NUMERIC — для форматирования чисел;
♦ locale.LC_TIME — для форматирования вывода даты и времени 
"""



print(locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8"))

lc = locale.setlocale (locale .LC_ALL, "") #Устаавливаем локаль по умолчанию
print(lc)

print(locale.getlocale()) # Получаем текущее значение локали для всех категорий




