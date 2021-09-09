# Статические методы

class Class:
    @staticmethod
    def func1(x, у ) : # Статический метод
        return x + у
    def func2(self, x, у): # Обычный метод в классе
        return x * у
    def func3(self, х, у):
        return Class.func1(х, у) # Вызов из метода класса

print(Class.func1(10, 20), end=" ") # Вызываем статический метод
c = Class()
print(c.func2(15, 6), end=" ") # Вызываем метод класса
print(c.func1(50, 12), end=" ") # Вызываем статический метод через экземпляр класса
print(c.func3(23, 5), end=" ") # Вызываем статический метод внутри класса

# Абстрактные методы

class Class1:

    def func(self, x ) : # Абстрактный метод
        # Возбуждаем исключение с помощью raise
        raise NotImplementedError("Необходимо переопределить метод")

class Class2(Class1): # Наследуем абстрактный метод
    def func(self, x ) : # Переопределяем метод
        print(x)

class Class3(Class1): # Класс не переопределяет метод
    pass

с2 = Class2()
с2.func(50) # Выведет: 50
сЗ = Class3()

try: # Перехватываем исключения
    сЗ.func(50) # Ошибка. Метод funcО не переопределен
except NotImplementedError as msg:
    print(msg) # Выведет: Необходимо переопределить метод