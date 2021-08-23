a, *b, c = ["hi", 2, 3, 4, 45, 567]

c = type(c)
b = type(b)


if isinstance(a, str): # Проверяет является ли переменная строкой
    print("String")

if c == int:
    print("Number")

if b == list:
    print("list")

# Операторы
x = 10
y = 5
i = x + y
print( "Сложение", i)

i = x - y
print("Вычитание",i)

i = x * y
print("Умножение *:",i)

i = x // y
print("Деление //:",i)

i = x % y
print("Остаток от деления %:",i)

i = x ** y
print("Возведение в степень **:",i)

""" 
(& = and) 
(| = or) (^ = or)

"""
y = 24
z = y << 1 # (<< 1) = (* 2)
print(z)
z = y >> 3 # (>> 1) = (/ 2) (>> 2) = (/ 4) (>> 3) = (/ 8)
print(z)
z = -z
print(z)

arr = [1, 2, 3, 4 , 5, "John"]

l = "John" in arr

print(l)

tpl = {"x": 132, "z": 23, "y": 132}

l = "x" in tpl, "y" in tpl, z in tpl # Поиск в кортеже значение x, y, z

print(l)

l = ("x" in tpl) is ("y" in tpl) # сравнивает

print(l)

arr = [1, 5, 3, 44, 7, 9]

arr.sort() # сортируем список

print(arr)

""" Логическое выражение можно инвентировать с помощью оперетора not"""
