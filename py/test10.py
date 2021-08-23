
for n in range(1, 11):
    print(n, end=" ")
else:
    print("\n Цикл выполнен")

for x in [1, 2, 3]:
    print(x, end= " ")
print()
for y in [1, 2, 3]:
    print(y, end= " ")
print()

arr = {"x": 1, "z": 3, "y": 2}

diArr = arr.keys() # Возвращает обьект который содержит все ключи
print(diArr)

for key in arr.keys(): # Используя словарь возвращает ключ при каждой итерации
    print(key, arr[key])

print()

for key in sorted(arr): # Сортировка ключей по алфовиту
    print(key, arr[key])

print()

arr = ([1, 34], [23, 45])

for a, b in arr: # Выводим елементы списка кортежей
    print(a, b)