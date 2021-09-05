def func():
    locall = 54
    glob2 = 25
    print("Локальные идентификаторы внутри функции")
    print(sorted(vars().keys()))
glob1, glob2 = 10, 88
func()
print("Глобальные идентификаторы вне функции")
print(sorted(vars().keys()))
print("Указание объекта в качестве параметра")
print(sorted(vars(dict).keys()))
print("Альтернативный вызов")
print(sorted(dict.__dict__.keys()))

def func_1(a):
    x = a
    def func_2(b):
        nonlocal x # Объявляем переменную как nonlocal
        print("x:", x)
        x = b # Можем изменить значение x в func_1 ()
    return func_2
f = func_1(10)
f(5) # 10

