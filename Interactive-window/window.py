import tkinter

from classes.Participant import Participant
from classes.Team import Team



# В этой функции будет происходить изменение данных в эксель, и, как я понимаю, снос имеющейся таблицы и создание новой с измененными данными
def apply_changes(entry_id, entry_name, entry_age, entry_sex, p: Participant):
    pass

def edit_menu(participant_to_edit : Participant):

    edit_window = tkinter.Tk()
    edit_window.minsize(250, 100)
    edit_window.title("Изменение участника команды")

    tkinter.Label(edit_window, text='Id').grid(row=0, column=0)
    tkinter.Label(edit_window, text="Name").grid(row=0, column=1)
    tkinter.Label(edit_window, text="Age").grid(row=0, column=2)
    tkinter.Label(edit_window, text="Sex").grid(row=0, column=3)

    edit_window.grid_columnconfigure(0, minsize=50)
    edit_window.grid_columnconfigure(1, minsize=50)
    edit_window.grid_columnconfigure(2, minsize=50)
    edit_window.grid_columnconfigure(3, minsize=50)
    edit_window.grid_columnconfigure(4, minsize=50)

    entry_id = tkinter.Entry(edit_window)
    entry_id.insert(-1, participant_to_edit.id)
    entry_id.grid(row=1, column=0)
    entry_name = tkinter.Entry(edit_window)
    entry_name.insert(-1, participant_to_edit.name)
    entry_name.grid(row=1, column=1)
    entry_age = tkinter.Entry(edit_window)
    entry_age.insert(-1, participant_to_edit.age)
    entry_age.grid(row=1, column=2)
    entry_sex = tkinter.Entry(edit_window)
    entry_sex.insert(-1, participant_to_edit.sex)
    entry_sex.grid(row=1, column=3)
    tkinter.Button(edit_window, command=lambda: apply_changes(entry_id, entry_name, entry_age, entry_sex, participant_to_edit), text="Сохранить").grid(row=1, column=4)

# Создаем функцию для создания таблицы
def create_table(team : Team, mainframe):
    frame = tkinter.Frame(mainframe)
    frame.pack(side=tkinter.LEFT)

    # Генерация шапки
    tkinter.Label(frame, text=team.team_name).grid(row=0, column=0, columnspan=4, stick="we")
    tkinter.Label(frame, text='Id').grid(row=1, column=0)
    tkinter.Label(frame, text="Name").grid(row=1, column=1)
    tkinter.Label(frame, text="Age").grid(row=1, column=2)
    tkinter.Label(frame, text="Sex").grid(row=1, column=3)

    frame.grid_columnconfigure(0, minsize=50)
    frame.grid_columnconfigure(1, minsize=50)
    frame.grid_columnconfigure(2, minsize=50)
    frame.grid_columnconfigure(3, minsize=50)
    frame.grid_columnconfigure(4, minsize=50)

    # Вывод участников команды
    for i in range(0, team.arr.__len__()):
        tkinter.Label(frame, text=team.arr[i].id).grid(row=i + 2, column=0)
        tkinter.Label(frame, text=team.arr[i].name).grid(row=i + 2, column=1)
        tkinter.Label(frame, text=team.arr[i].age).grid(row=i + 2, column=2)
        tkinter.Label(frame, text=team.arr[i].sex).grid(row=i + 2, column=3)
        tkinter.Button(frame, text="Edit", command=lambda: edit_menu(team.arr[i])).grid(row=i + 2, column=4)


def create_window(teams_arr: list):

    # Создаем главное окно
    root = tkinter.Tk()
    root.minsize(700, 250)
    root.title("Таблицы с названиями команд и списками участников")

    # Здесь должны находиться все фреймы, относящиеся к командам
    mainframe = tkinter.Frame(root)
    mainframe.pack(side="top", anchor="w")

    for i in range(0, teams_arr.__len__()):
        create_table(teams_arr[i], mainframe)

    # Запускаем главный цикл обработки событий
    root.mainloop()


part1 = Participant(1, "Dima", 20, "M")
part2 = Participant(2, "Yana", 21, "Z")
team1 = Team([part1, part2])
team2 = Team([part2, part1])
team3 = Team([part2, part1])
team4 = Team([part2, part1])

teams = [team1, team2, team3, team4]

create_window(teams)


