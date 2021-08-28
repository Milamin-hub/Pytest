print("Введите слово 'stop' для получения результата")
summa = 0

while True:
    x = input("Введите число: ")
    if x == "stop": break
    if x == "":
        print("Вы не ввели значение")
        continue
    if x[0] == "-":
        if not x[1:].isdigit():
            print("Необходимо ввести число, а не строку!")
            continue
    else:
        if not x.isdigit():
            print("Необходимо ввести число, а не строку!")
            continue
        
    summa += int(x)
print("Сумма чисел: ", summa)
    
