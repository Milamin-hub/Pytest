from functools import reduce
import random

def func(x, y):
    print ("({0}, {1})".format(x, y), end=" ")
    return x + y
l_1 = [1, 2, 3, 4, 5]
summa = reduce(func, l_1)
print()
print("Сумма последовательности: ", summa)

# remove(3начение) — удаляет первый элемент, содержащий указанное значение.



# count() - общее количество элементов с указанным значением

l_2 = [1, 2, 3, 4, 3, 5, 6, 2]
k_1 = min(l_2), max(l_2)
print("min, max:", k_1)
l_3 = []
for i in range(len(l_2)):
    l_3 += ["%s" % l_2[i] + ": " + "%s" % l_2.count(l_2[i])]
print(l_3) 

# any() возвращает значение True, если в последовательности существует хотя бы один элемент

print(any([0, None])) # false

# ♦ all() возвращает True, если все элементы последовательности  возвращают значение True или последовательность
# не содержит элементов

print(any([])) # false

# sample() — возвращает список из указанного количества элементов

l_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n_1 = random.sample(l_4, len(l_4))
print(n_1)
l_4.sort(reverse=True)
print(l_4)