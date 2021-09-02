from timeit import Timer

# timeit - позволяет измерить время выполнения небольших фрагментов кода с целью оптимизации программы

# Timer([stmt= 'pass'] [, setup = 'pass'] [, timer = <timer function>])

# В параметре stmt указывается код (в виде строки), время выполнения которого измеряется

# Параметр setup позволяет указать код, который будет выполнен перед измерением времени

code1 = """\
i = 1
j = 0
while i < 10001:
    j += i
    i += 1
"""
t1 = Timer(stmt=code1)
print("while: ", t1.timeit(number = 10000)) # Время выполнения цикла while 11.9 секунд
code2 = """\
j = 0
for i in range(1, 10001):
    j += i
"""
t2 = Timer(stmt=code2)
print("for: ", t2.timeit(number = 10000)) # Время выполнения цикла for 7.7 секунд
code3 = """\
j = sum(range(1, 10001))
"""
t3 = Timer(stmt=code3)
print("sum: ", t3.timeit(number = 10000)) # Время выполнения функции sum 2.2 секунд