msg = "Модуль {0}".format(__name__)

class d_txt:
    """ Строка документирования """
    print("Инструкция выполняется немедленно")

# Создание атрибута и метода

class MyClass:
    def __init__(self): # Конструктор
        self.x = 10 # Атрибут экземпляра класса
c = MyClass() # Создание экземпляра класса
print(c.x) # К атрибуту можно обратиться непосредственно

# ♦ getattr () — возвращает значение атрибута по его названию, заданному в виде строки. 
# ♦ setattr () — задает значение атрибута. Название атрибута указывается в виде строки. 
# ♦ delattr(<Объект>, <Атрибут>) — удаляет атрибут, чье название указано в виде строки;
# ♦ hasattr (<осъект>, <Атрибут>) — проверяет наличие указанного атрибута. Если атрибут
# существует, функция возвращает значение True.

print(getattr(c, "x"))
setattr(c, "у", 20) 
print(getattr(c, "у"))
print(hasattr(c, "x"))

c_1 = MyClass()
c_2 = MyClass()
c_1.x = 22
c_2.x = 33
print(c.x, c_1.x, c_2.x)

class MyClass_1:
    def __init__(self, valuel, value2): # Конструктор
        self.x = valuel
        self.y = value2
    def __del__(self): # Деструктор класса
        print("Вызван метод del ()")
c_3 = MyClass_1("10", "20")
print(c_3.x, c_3.y)
del c_3
try:
    print(c_3)
except NameError:
    print("Экземпляр удален или не найден")

class Myclass_3():
    def d_1(self):
        print("Метод функции d_1")

class Myclass_2(Myclass_3): # Наследование
    def d_2(self):
        print("Метод функции d_2")

c_4 = Myclass_2()
c_4.d_1()
c_4.d_2()

class Classl: x = 10
class Class2(Classl): pass
class Class3(Class2): pass
class Class4(Class3): pass
class Class5(Class2): pass
class Class6(Class5): pass
class Class7(Class4, Class6): pass
c = Class7 ()
print(c.x)

print(Class7.__mro__) # Последовательность поиска атрибута x


