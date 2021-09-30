import test46
from tkinter import *
from tkinter.ttk import Combobox 
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from os import path

def clicked():
    # Выводим введенный текст
    res = "%s" % Drop_downList.get() + " hello %s" % txt_input.get()
    add_text.configure(text=res)

def clicked_1():
    messagebox.showinfo("Greed", "Hello") # 1 кнопка "Ок"
    messagebox.askquestion('Заголовок', 'Текст') # 2 кнопки "Да" или "Нет"
    messagebox.askyesnocancel('Заголовок', 'Текст') # 3 кнопки "Да", "Нет", "Отмена"
    messagebox.askretrycancel('Заголовок', 'Текст') # 2 кнопки "Повторить", "Отмена"

def clicked_2():
    i = 0
    while i < 101:
        i += 1
        bar["value"] += 1
        

# Создание окна
window = Tk()
# Название окна
window.title("Window")
# Меняем размер окна
window.geometry('500x600')
# Добавление текста, меняем стиль шрифта и размер
add_text = Label(window, text="Привет", font=("Arial Bold", 15))
# Указываем координты(без функции grid текст не будет отображаться)
add_text.grid(column=1, row=0)
# Создать кнопку, bg - поменять фон кнопки, fg - поменять цвет текста кнопки
button = Button(window, text="Начать", bg="gray", fg="white", command=clicked)
button.grid(column=3, row=0)
# Пользовательский ввод
txt_input = Entry(window, width=10)
# Дает возможность сразу написать текст
txt_input.focus()
txt_input.grid(column=2, row=0)
# Виджет поля с выпадающем списком
Drop_downList = Combobox(window)
# Значения в выпадающем списке
Drop_downList["values"] = (1, 2, 3)
# Вариант по умолчанию 
Drop_downList.current(1)
Drop_downList.grid(column=1, row=2)
# Задаем тип boolean
status_button = BooleanVar() # IntVar - .set(0) False, .set(1) True
# Проверка состояния чекбокса
status_button.set(False)
# Чекбокс
check_button = Checkbutton(window, text="check", var=status_button)
check_button.grid(column=2, row=2)
status_radiobutton = BooleanVar()
status_radiobutton.set(False)
# Радио кнопка
radio_button_1 = Radiobutton(window, text="first", value=1, var=status_radiobutton)
# Задать command любой из этих кнопок для определенной функции.
radio_button_2 = Radiobutton(window, text="second", value=2, var=status_radiobutton)
radio_button_3 = Radiobutton(window, text="third", value=3, var=status_radiobutton)
radio_button_1.grid(column=1, row=3)
radio_button_2.grid(column=2, row=3)
radio_button_3.grid(column=3, row=3)
# Текстовое поле
scrolled_txt = scrolledtext.ScrolledText(window, width=30, height=10)
scrolled_txt.insert(INSERT, " Текстовое поле")
scrolled_txt.grid(column=1, row=4)
# messagebox.showinfo - всплывающее окно
# messagebox.showwarning - показывает предупреждающее сообщение
# messagebox.showerror - показывает сообщение об ошибке
button_1 = Button(window, text="Начать", bg="gray", fg="white", command=clicked_1)
button_1.grid(column=1, row=5)
# Указываем начальное значение
var = IntVar()
var.set(35)
# Диалоговое окно
# Передаем параметры from_ и to, Чтобы указать диапазон номеров
spin = Spinbox(window, from_=0, to=100, width=10, textvariable=var) 
spin.grid(column=1, row=6)
# Индикатор загрузки
bar = Progressbar(window, length=100)
# Прогресс
bar["value"] = 0
button_1 = Button(window, text="Закончить прогресс", bg="gray", fg="white", command=clicked_2)
button_1.grid(column=2, row=7)
bar.grid(column=1, row=7)
# запрашивает файл
file_path = filedialog.askopenfilename()
# Указываем тип предпочитаемого файла
file_path = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
# Получаем путь и имя файла который выбрали
print(file_path)
dir_path = filedialog.askdirectory()
# Получаем путь дириктории
print(dir_path)
# Указать начальную директорию initialdir
file_2 = filedialog.askopenfilename(initialdir= path.dirname(__file__))
print(file_2)
# Зацикливание
window.mainloop()