import re

# I или ignorecase — поиск без учета регистра:

p = re.compile(r"^[а-яе]+$", re.U) 
print("Найдено" if p.search("абв") else "Нет") # Поиск по регистру

p = re.compile(r"^[а-яе]+$", re.I | re.U) 
print("Найдено" if p.search("АБагд") else "Нет") # Поиск по регистру

# Символ ^ соответствует привязке к началу каждой подстроки;
# Cимвол $ — позициия перед символом перевода строки;

c = re.compile(r"""^# Привязка к началу строки
[0-9]+ #Строка должна содержать одну цифру (или более)
$ # Привязка к концу строки 
""", re.X| re.S)
print("Найдено" if c.search("124245021") else "Нет") # Найдено

