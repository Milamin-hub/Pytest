# Получение информации об исключении

try:
    х = 1 / 0 # Ошибка деления на О
except (NameError, IndexError, ZeroDivisionError) as err :
    print(err. __class__.__name__) # Название класса исключения
    print(err) 

print("Введите слово 'stop' для получения результата")
summa = 0
while True:
    x = input( "Введите число: ")
    if x == "stop":
        break # Выход из цикла
    try:
        х = int(x) # Преобразуем строку в число
    except ValueError:
        print( "Необходимо ввести целое число !")
    else :
        summa += х
print("Сумма чисел равна:", summa)


v_1 = input("Введите файл который хотите создать: ")
with open("test{0}.py".format(v_1), "a", encoding="utf-8") as f:
    f.write("import sys\n") # Записываем строку в конец файла
