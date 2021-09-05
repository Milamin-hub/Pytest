import time, sys

def update_progress(progress):
    barLength = 10 # Длина индикатора выполнения
    block = int(round(barLength*progress)) # (10 * (0.n => 1))
    text = "\rloading[{0}] {1}%".format( "#"*block + "-"*(barLength-block), int(progress*100)) # 1."" 2.[] 3.n%
    sys.stdout.write(text) # Выводим результат => loading[] n%
    sys.stdout.flush() # Собирает данные "written" для стандартного выхода, прежде чем записать их в terminal
print()

u = update_progress

def loading(update_progress): # Подключаем функцию update_progress
    for i in range(101):
        time.sleep(0.1) # Задержка
        update_progress(i/100.0) # => progress
    print()

    print("Test completed")
    time.sleep(2)

loading(u)