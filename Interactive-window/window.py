import tkinter
from tkinter import ttk

from classes.Participant import Participant
from classes.Team import Team


# Создаем главное окно
root = tkinter.Tk()
root.minsize(700, 250)
root.title("Таблицы с названиями команд и списками участников")


# Создаем функцию для создания таблицы
def create_table(frame, title, table : Team):
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

#frame1 = tkinter.Frame(root)
#frame1.pack(side=tkinter.LEFT)
#create_table(frame1, "Команда 1", tabla)

mainframe = tkinter.Frame(root)
mainframe.pack(side="top", anchor="w")
# Создаем фреймы для каждой таблицы
frame1 = tkinter.Frame(mainframe)
frame1.pack(side=tkinter.LEFT)
create_table(frame1, "Команда 1",tabla)

frame2 = tkinter.Frame(mainframe)
frame2.pack(side=tkinter.LEFT)
create_table(frame2, "Команда 2",tabla)

frame3 = tkinter.Frame(mainframe)
frame3.pack(side=tkinter.LEFT)
create_table(frame3, "Команда 3",tabla)

# Запускаем главный цикл обработки событий
root.mainloop()
