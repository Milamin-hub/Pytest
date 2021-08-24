arr = [1, 3, 6, 7, 9 , 10]

"""
range ([<Начало>, ]<Конец>[, <Шаг>])
len() # Количество элементов списка
"""

for i in range(len(arr)):
    arr[i]

print(arr)

for i in range(2, 101, 2):
    print(i, end=" ") # Выводим четныя числа 1 до 100

print()

obj = range(len([1, 5, 5, 6]))

print(obj) # range(0, 4) срез


i = iter(obj)
print(next(i), next(i), next(i)) # поиск по индексу

sObj = obj[0:2]
print(sObj) 

arr = list(obj)
print(arr) # Преобразование диапазона в список

obj = range(1, 5)
objI = obj.index(1), obj.index(4) # возвращает индекс элемента
print(objI)

objC = obj.count(1), obj.count(5) # возвращает количество элементов с указанным значением
print(objC)

array = [1, 2, 3, 4, 5, 6, 7, 8]

for i, elem in enumerate(array): # На каждой итерации цикла for возвращает кортеж из индекса и значения текущего элемента
    if elem % 2 == 0: # Проверка на четное число
        array[i] *= 2 # Умножаем каждый второй елемент на два

print(array) 