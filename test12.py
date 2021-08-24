"""
while <Условие>:
<Инструкции>
<Приращение значения в переменной-счетчике>
[else :
< Блок, выполняемый, если не использовать break>
"""

"""
i = 100
while i: # условие не содержит оператор сравнения. когда переменная-счетчик становится нулем, то условие заверщается (0 ~ false)
    print(i, end=" ")
    i -= 1
print()
"""

"""
arr = [1, 2, 4, 6, 7]
i = 0
while i < len(arr): # Перебор массива
    arr[i] *= 2
    print(arr[i], end=" ")
    i += 1
print()
"""

""" continue """

"""
for i in range(1, 21): # Выводим все числа кроме от 6 до 14
    if 5 < i < 15:
        continue # Переходим на следующую итерацию цикла
    print(i, end=" ")
print()
"""

""" break """

"""
i = 1
while True:
    if i > 10: break
    print(i, end=" ")
    i += 1 
print()
"""

print("Введите слово 'stop' для получения результата")
summa = 0
while True:
    x = input("Введите число: ")
    if x == "stop": break
    summa += int(x)
print("Результат: ", summa)
