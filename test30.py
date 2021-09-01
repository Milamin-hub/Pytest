import itertools

# ♦ itertools содержит функции, позволяющие генерировать различные последовательности на основе 
# других последовательностей

# count() — создает бесконечно нарастающую последовательность значений

for i in itertools.count():
    if i > 10: break
    print(i, end=" ")
print()

n = 1
for i in itertools.cycle("abc"):
    if n > 10: break
    print(i, end=" ")
    n += 1
print()

s_l = list(zip(itertools.cycle([0, 1]), "абвгд"))
print(s_l)

# repeat() — возвращает объект указанное количество раз

s_r = list(itertools.repeat(1, 5))
print(s_r)

# combinations() — на каждой итерации возвращает кортеж, содержащий комбинацию из количества элементов.

l_c =list(itertools.combinations('абвг', 2))
print(l_c)

def func(x): return x > 3
l_f = list(itertools.filterfalse(func, [4, 5, 6, 0, 7 , 2 , 3]))
print(l_f)

l_a = list(itertools.accumulate([1, 2, 3, 4, 5, 6])) # На каждой итерации добавляет придыдущий результат 
print(l_a)

