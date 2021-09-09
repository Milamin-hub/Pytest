from abc import ABCMeta, abstractmethod

class Class1(metaclass=ABCMeta):
    @abstractmethod
    def func(self, x ) : # Абстрактный метод
        pass
class Class2(Class1): # Наследуем абстрактный метод
    def func(self, x) : # Переопределяем метод
        print(x)
class Class3(Class1): # Класс не переопределяет метод
    pass
        
c2 = Class2()
c2.func(50) # Выведет: 50
try:
    сЗ = Class3() # Ошибка. Метод func() не переопределен
    сЗ.func(50)
except TypeError as msg:
    print(msg) 

# Свойства класса

class Class_1:
    def __init__(self, value):
        self.__var = value
    def get_var(self): # Чтение
        return self.__var
    def set_var(self, value): # Запись
        self.__var = value
    def del_var(self): # Удаление
        del self.__var
    v = property(get_var, set_var, del_var, "Строка документирования")
c_1 = Class_1(5)
c_1.v = 35 # Вызывается метод set_var()
print(c_1.v) # Вызывается метод get_var()
del c_1.v # Вызывается метод del_var()

# Декоратор класса

def deco(C): # Принимает объект класса
    print("Внутри декоратора число:", end=" ") # Производит какие-то действия
    return C # Возвращает объект класса
@deco
class MyClass:
    def __init__(self, value) :
        self.v_1 = value
c = MyClass(5)
print(c.v_1)