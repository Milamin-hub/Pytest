"""Это описание нашего модуля"""

def fun():
    """Это описание нашей функции"""
    pass

arr = range(1, 6)

i = iter(arr)

n = 1
while n < 6:
    nxt = next(i)
    n += 1 
    print(nxt, end=" ")

print()

d = {"z": 5, "q": 28 }

s = iter(d)

nx = s.__next__() # Возвращает ключ

nt = d[s.__next__()] # Получаем значение по ключу

print(nt)
print(nx)

for i in [32, 49]:
    print(i)

for i in "Строка":
    print(i, " -", end=" ")