import test46
import sched
import time

# ♦ Планировщик заданий - высокоуровневое средство поможет, если нужно
# выпол­нить в параллельном потоке последовательность каких-либо задач(заданий).

# ♦ enterabs(<Время>,<Приоритет>,<Функция>[,argument=()][,kwargs={}]) — создает 
# задание, запускаемое в точно заданное время, которое указано первым параметром, 
# с приоритетом из второго параметра.

# ♦ enter(<3адержка>,<Приоритет>,<Функция>[,argument=()][,kwargs=()]) — 
# создает задание, запускаемое спустя указанную первым параметром задержку,
# с приоритетом из второго параметра.

# ♦ run([biocking=True]) — запускает на выполнение все созданные в текущем
# планиров­щике задания. Параметр blocking задает режим их выполнения

# ♦ cancel(<3адание>) — отменяет указанное в параметре задание.

# ♦ empty() — возвращает True, если в планировщике нет заданий 
# (еще не добавлены или уже все выполнены), и False в противном случае.

def print_time(thread_num):
    t = time.strftime("%H:%M:%S", time.localtime(time.time()))
    print("Задание {0}: {1}".format(thread_num, t))

task = sched.scheduler()
task.enterabs(time.monotonic() + 2, 1, print_time, argument=(1,))
task.enter(3, 1, print_time, argument=(2,))
task.enter(3, 2, print_time, argument=(3,))
task.run()

# Вывод:
# Задание 1: 23:22:18 
# Задание 2: 23:22:19 
# Задание 3: 23:22:19