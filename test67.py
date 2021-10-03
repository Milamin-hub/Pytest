import test46
import threading
import time

# Применение событий

def task1() :
    global evt
    print("Поток 1 начал работу" )
    time.sleep(3)
    print("Поток 1 инициировал возникновение события")
    evt.set()
def task2():
    global evt
    print("Поток 2 начал работу")
    evt.wait()
    print("Поток 2 инициировал возникновение события")
evt = threading.Event()
thread1 = threading.Thread(target=task1)
thread1.start()
thread2 = threading.Thread(target=task2)
thread2.start()