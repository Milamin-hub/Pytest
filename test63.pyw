import test46
from tkinter import *
from tkinter import Menu
from tkinter import ttk

window = Tk()
window.title("Test")
window.geometry("300x200")

# Добавление панели меню
menu = Menu(window, bg="gray", fg="white")
new_item = Menu(menu, tearoff=0, bg="gray", fg="white")
# .add_command - Создает пункт меню
new_item.add_command(label="create")
# .add_separator - разделяет линией пункты
new_item.add_command(label="change")
menu.add_cascade(label="file", menu=new_item)
# .add_cascade - Создает подменю
menu.add_cascade(label="author")
# Выводит на экран
window.config(menu=menu)

# Управление вкладками

# создается элемент управления вкладкой
tab_control = ttk.Notebook(window)
# создается вкладка
tab_1 = ttk.Frame(tab_control, width=20)
tab_2 = ttk.Frame(tab_control, width=20)

# Добавление виджетов во вкладки
label_1 = Label(tab_1, text='first tab', padx=5, pady=5)
label_1.grid(column=1, row=1)
label_2 = Label(tab_2, text='second tab', padx=5, pady=5)
label_2.grid(column=1, row=1)

# Добавляем элемент в управление вкладками
tab_control.add(tab_1, text="first")
tab_control.add(tab_2, text="second")
# Запаковываем элементы в управление вкладками
# чтобы они стали видимыми в окне 
tab_control.pack(expand=1, fill="both")

# Метакласс

# ♦ stringVar - хранит строковое значение (тип str);
# ♦ intvar — хранит целое число (тип int);
# ♦ DoubleVar — хранит вещественное число (тип float);
# ♦ BooleanVar — хранит логическую величину (тип boolean).

# Методы

# ♦ get() — возвращает значение, хранящееся в метапеременной;
# ♦ set() — заносит значение в метапеременную.

# События

# ♦ Button - Нажатие кнопки мыши 
# ♦ ButtonRelease - Отпускание ранее нажатой кнопки мыши 
# ♦ MouseWheel - Вращение колесика мыши на компоненте 
# ♦ Enter - Наведение курсора мыши на компонент 
# ♦ Motion - Перемещение курсора мыши внутри компонента 
# ♦ Leave - Увод курсора мыши с компонента 
# ♦ KeyPress - Нажатие клавиши 
# ♦ KeyRelease - Отпускание ранее нажатой клавиши 
# ♦ FocusIn - Получение компонентом фокуса ввода 
# ♦ FocusOut - Потеря компонентом фокуса ввода 
# ♦ Activate - Изменение состояния компонента с недоступного для ввода
# (такой компонент закрашен серым) на доступное
# ♦ Deactivate - Изменение состояния компонента с доступного для ввода на недоступное
# ♦ Мар - Помещение компонента в контейнер с применением одного из диспетче­ров компоновки
# ♦ Unmap - Удаление компонента из контейнера
# ♦ Expose - Компонент или окно, в котором он находится (или их части), стали видимыми
# ♦ Visibility - Окно (или его часть), в котором находится компонент, стало видимым 
# ♦ Configure - Изменение размеров компонента (например, вследствие изменения размеров окна)
# ♦ Destroy - Уничтожение компонента

# Модификаторы

# Double - Событие должно возникнуть дважды в течение короткого промежутка времени
# Triple - Событие должно возникнуть трижды в течение короткого промежутка времени
# Shift - Должна удерживаться клавиша <Shift>
# Control - Должна удерживаться клавиша <Ctrl>
# Alt - Должна удерживаться клавиша <Alt>
# Any - Отсутствие любых дополнительных условий



window.mainloop()