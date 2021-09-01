# Перебрать элементы множества позволяет цикл for

for i in set([9, 7, 5]): print(i, end=" ")
print()

# union() и |  — объединяют два множества:

s = set([1, 2, 3])
print(s | (set([4, 5, 6])))

# ♦ a |= b и а. update(b) — добавляют элементы множества b во множество а

s |= set([7, 8, 9])
print(s)

# ♦ - и difference() — вычисляют разницу множеств:
j = set([1, 2, 3])
a = set([1, 2, 3])
i = set([i]) 
print(s - a)

# а -= b и a.difference update(b) — удаляют элементы из множества а, которые существуют и во множестве а, и во множестве b:
j.difference_update(a)
print(j.difference_update(a)) 

# ♦ & и intersection!) — пересечение множеств. 

l_s_a = a <= j # Сравнивает
print(l_s_a)