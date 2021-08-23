import sys
import test6
import keyword
import builtins

arr = sys.argv[:] # Сохраняет в переменную имя файла
for n in arr:
    print(n)

""" Замисть help используем doc"""

print(test6.__doc__) 
print(test6.fun.__doc__)

print(dir(test6)) # dir() получаем список всех индентификаторов

key_word = keyword.kwlist

input("Enter")

print(key_word) # Вызывает ключевые слова

input("Enter")

fck = dir(builtins)

print(fck) # Вызов встроенных индентификаторов

input("Enter")

