n = eval("20 / 20") # eval (),принимает параметр строки и возвращает вычисление
print("Значение: ", n)

arr1 = [0, 1, 4, 3]
arr1.append(2) # Добавляет элемент в конец
arr1.sort() # Сортирует массив
print(arr1)

arr1.insert(0, 23) # Добавляет элемент в указанную позицию
print(arr1)

arr1.pop(0) # Удаляет элемент по индексу
print(arr1)

del arr1[:2] # удаляет с первый и второй элемент
print(arr1)

arr1.remove(4) # удаляет первай элемент по значению
print(arr1)

arr1.reverse() # изменяет порядок следования элементов на противоположный
print(arr1)
