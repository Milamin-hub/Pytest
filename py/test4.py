import sys

for n in range(1, 5):
    print(n, end = " ")

print()

print("Этот текст с новой строки")

sys.stdout.write("Строка1\n")
sys.stdout.write("Строка2\n")

name = input("Введите имя: ")
print("Hello", name)
input("Нажмите Enter")

try:
    s = input("введите s: ")
    print(s)
except EOFError:
    print("Обработали исключение EOFError")