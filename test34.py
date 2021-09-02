import calendar, locale

# ♦ Textcalendar — позволяет вывести календарь в виде простого текста

c_1 = calendar.TextCalendar(0)
print(c_1.formatyear(2021)) # Текстовый календарь на 2021 год

с_2 = calendar.HTMLCalendar(0) # позволяет вывести календарь в формате HTML
print(с_2.formatyear(2017))

c_3 = calendar.LocaleTextCalendar(0, "ru_RU.UTF-8")
print(c_3.formatmonth(2021, 9))

# ♦ formatyear()— возвращает текстовый календарь на указанный год.

# • w — ширина поля с днем (по умолчанию 2);
# • 1 — количество символов перевода строки между строками (по умолчанию 1 );
# • с — количество пробелов между месяцами (по умолчанию 6);
# • m — количество месяцев на строке (по умолчанию 3).

print(c_1.formatyear(2021))

с_4 = calendar.HTMLCalendar(0)
print(с_4.cssclasses[0]) # список названий для каждого дня недели: mon

# ♦ formatyearpage() — возвращает календарь на указанный год в виде отдельной веб-страницы.

# • width — количество месяцев на строке (по умолчанию 3)
# • css — название файла с таблицей стилей (по умолчанию "calendar.css")
# • encoding — кодировка файла. Название кодировки будет указано в параметре encoding XML-пролога,
# а также в теге <meta>

xhtml = с_4.formatyearpage(2017, 4, encoding="UTF-8")
print(type(xhtml))
print(xhtml.decode("utf-8")) # html calendar

cw_1 = calendar.weekheader(3)
print(cw_1) # Mon Tue Wed Thu Fri Sat Sun

locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")
cw_2 = calendar.weekheader(2)
print(cw_2) # Пн Вт Ср Чт Пт Сб Вс

# ♦ day_name — список полных названий дней недели в текущей локали:

print([i for i in calendar.day_name])
