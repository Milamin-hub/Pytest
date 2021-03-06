import math as Math
""" Math """

print("e: ", Math.e)
print("pi: ", Math.pi)

""" 
♦ sin (), cos (), tan () — стандартные тригонометрические функции (синус, косинус, тангенс).
Значение указывается в радианах;
♦ asin (), acos (), atan () — обратные тригонометрические функции (арксинус, арккосинус,
арктангенс). Значение возвращается в радианах;
♦ degrees () — преобразует радианы в градусы:
"""

Gs = Math.degrees(Math.pi) # преобразует радианы в градусы
print("Градусы: ", Gs)

Rs = Math.radians(Gs) # — преобразует градусы в радианы
print("Радианы: ", Rs)

"""
♦ exp() - Экспонента
♦ log (<Число> [, <База>]) — логарифм по заданной базе. Если база не указана, вычисляется натуральный логарифм (по базе е)
♦ log10 ( ) — десятичный логарифм
♦ 1оg2 () — логарифм по базе 2
♦ sqrt () — квадратный корень
"""
sq = Math.sqrt(100), Math.sqrt(25) # Возводим корень квадратный
print("Квадратный корень: ", sq)

""" ceil () — значение, округленное до ближайшего большего целого """

z = Math.ceil(2.4) # , Округленное до ближайшего большего
print("Округление до большего числа: ", z)

""" floor() — значение, округленное до ближайшего меньшего целого """


z = Math.floor(2.6) # , Округленное до ближайшего меньшего
print("Округление до меньшего числа: ", z)

""" fmod () - остаток от деления """

z = Math.fmod(7, 3) # , Остаток от деления
print("Остаток от деления: ", z)

""" factorial () — факториал числа """

z = Math.factorial(4) # , Остаток от деления
print("факториал числа: ", z)

""" fsum(<cnncoK чисел>) — возвращает точную сумму чисел из заданного списка """

z = Math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
print("Сумма: ", z)