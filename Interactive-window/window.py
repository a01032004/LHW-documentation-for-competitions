import tkinter
from tkinter import ttk

from classes.Participant import Participant
from classes.Team import Team


# Создаем главное окно
root = tkinter.Tk()
root.minsize(700, 250)
root.title("Таблицы с названиями команд и списками участников")

# Здесь должны находиться все фреймы, относящиеся к командам
mainframe = tkinter.Frame(root)
mainframe.pack(side="top", anchor="w")


# Создаем функцию для создания таблицы
def create_table(title, table : Team):
    frame = tkinter.Frame(mainframe)
    frame.pack(side=tkinter.LEFT)

    label0 = tkinter.Label(frame, text=title)
    label1 = tkinter.Label(frame, text='id')
    label2 = tkinter.Label(frame, text="name")
    label3 = tkinter.Label(frame, text="age")
    label4 = tkinter.Label(frame, text="sex")

    label0.grid(row=0, column=0, columnspan=4,stick="we")
    label1.grid(row=1, column=0)
    label2.grid(row=1, column=1)
    label3.grid(row=1, column=2)
    label4.grid(row=1, column=3)

    frame.grid_columnconfigure(0, minsize=50)
    frame.grid_columnconfigure(1, minsize=50)
    frame.grid_columnconfigure(2, minsize=50)
    frame.grid_columnconfigure(3, minsize=50)

    for i in range(0, table.arr.__len__()):
        tkinter.Label(frame, text=table.arr[i].id).grid(row=i + 2, column=0)
        tkinter.Label(frame, text=table.arr[i].name).grid(row=i + 2, column=1)
        tkinter.Label(frame, text=table.arr[i].age).grid(row=i + 2, column=2)
        tkinter.Label(frame, text=table.arr[i].sex).grid(row=i + 2, column=3)


def create_window():
    pass


part1 = Participant("M", 20, "Dima", 1)
part2 = Participant("Z", 21, "Yana", 2)

tabla = Team([part1, part2])


# Создаем фреймы для каждой таблицы
create_table("Команда 1", tabla)

create_table("Команда 2", tabla)

create_table("Команда 3", tabla)

# Запускаем главный цикл обработки событий
root.mainloop()
