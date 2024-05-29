import tkinter
from tkinter import ttk

# Создаем главное окно
root = tkinter.Tk()
root.title("Таблицы с названиями команд и списками участников")

# Создаем функцию для создания таблицы
def create_table(frame, title):
    label = tkinter.Label(frame, text=title)
    label.pack()

    tree = ttk.Treeview(frame)
    tree["columns"] = ("name", "age")  # Задаем столбцы таблицы
    tree.column("#0", width=100, minwidth=100)
    tree.column("name", anchor=tkinter.W, width=100)
    tree.column("age", anchor=tkinter.W, width=100)

    tree.heading('#0', text='ID', anchor=tkinter.W)
    tree.heading('name', text='Имя', anchor=tkinter.W)
    tree.heading('age', text='Возраст', anchor=tkinter.W)

    tree.pack()
