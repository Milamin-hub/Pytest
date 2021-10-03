import test46
import threading
import random
import time

# Низкоуровневые средства для многопоточных вычислений.

# ♦ Для представления отдельного потока, выполняющего
# какую-либо задачу, служит класс Thread.

def task(count=10):
    for i in range(1, count + 1):
        n = random.randint(1, count)
        time.sleep(n)
        print("Значение {0}: {1}".format(i, n))

thread = threading.Thread(target=task, kwargs={"count": 5})
"""thread.start()"""

class TestThread(threading.Thread):
    def __init__(self, count=10):
        super().__init__()
        self.count = count

    def run(self):
        for i in range(1, self.count + 1):
            n = random.randint(1, self.count)
            time.sleep(n)
            print("Значение {0}: {1}".format(i, n))

thread = TestThread(count=5)
""" thread.start()"""

# Использование блокировок

# Класс Lock поддерживает три метода:

# acquire([blocking=True][,][timeout=-1])— накладывает блокировку.
# release() — снимает блокировку.
# locked() — возвращает True, если блокировка была наложена,
# и False — в противном случае.

lock = threading.Lock()

thread1 = TestThread(count=5)
thread1.start()
thread2 = TestThread(count=5)
thread2.start()

# Рекурсивную блокировку представляют классом RLock.

# Если простая блокировка одним и тем же потоком может быть
# наложена всего один раз, то рекурсивная — сколько угодно.

# Кондиция - позволяет приостановить второй поток пока не закончится первый 
# Нужно если выполнения одного потока является значение,
# которое ис­пользует в работе другой поток

# Кондиция представляется классом Condition, Condition([lock=None])

def task1():
    global val, cond
    cond.acquire()
    while not val:
        cond.wait()
    print(val)
    val = None
    cond.release()

def task2():
    global val, cond
    time.sleep(3)
    cond.acquire()
    val = "Подъем!!!"
    cond.notify()
    cond.release()

val = None
cond = threading.Condition()
thread1 = threading.Thread(target=task1)
thread1.start()
thread2 = threading.Thread(target=task2)
thread2.start()