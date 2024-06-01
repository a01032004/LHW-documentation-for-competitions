import tkinter

from classes.Participant import Participant
from classes.Team import Team



# В этой функции будет происходить изменение данных в эксель, и, как я понимаю, снос имеющейся таблицы и создание новой с измененными данными
def apply_changes(entry_id, entry_name, entry_age, entry_sex, p: Participant, window):
    if p.name == "":# это добавление
        pass
    else:# это изменение
        pass
    window.destroy()


def  window_rebuild(root, teams_arr):
    root.destroy()
    create_window(teams_arr, True)


def edit_time_menu(participant_to_edit : Participant):
    edit_window = tkinter.Tk()
    edit_window.minsize(250, 100)
    edit_window.title("Изменение времени участника")

    tkinter.Label(edit_window, text='start').grid(row=0, column=0)
    tkinter.Label(edit_window, text="finish").grid(row=0, column=1)
    edit_window.grid_columnconfigure(0, minsize=75)
    edit_window.grid_columnconfigure(1, minsize=75)

    entry_start = tkinter.Entry(edit_window)
    entry_start.grid(row=1, column=0)
    entry_finish = tkinter.Entry(edit_window)
    entry_finish.grid(row=1, column=1)

    entry_start.insert(-1, participant_to_edit.start_time)
    entry_finish.insert(-1, participant_to_edit.finish_time)

    tkinter.Button(edit_window).grid(row=1, column=2)

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
    entry_id.grid(row=1, column=0)
    entry_name = tkinter.Entry(edit_window)
    entry_name.grid(row=1, column=1)
    entry_age = tkinter.Entry(edit_window)
    entry_age.grid(row=1, column=2)
    entry_sex = tkinter.Entry(edit_window)
    entry_sex.grid(row=1, column=3)

    if participant_to_edit.id != -1:
        entry_id.insert(-1, participant_to_edit.id)
    entry_name.insert(-1, participant_to_edit.name)
    if participant_to_edit.age != -1:
        entry_age.insert(-1, participant_to_edit.age)
    entry_sex.insert(-1, participant_to_edit.sex)

    tkinter.Button(edit_window, command=lambda: apply_changes(entry_id, entry_name, entry_age, entry_sex, participant_to_edit, edit_window), text="Сохранить").grid(row=1, column=4)


# Создаем функцию для создания таблицы
def create_table(team: Team, mainframe, is_end: bool, frame_row: int, frame_column: int):
    frame = tkinter.Frame(mainframe, padx=5, pady=5)
    frame.grid(row=frame_row, column=frame_column)

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
        if not is_end:
            tkinter.Button(frame, text="Edit", command=lambda: edit_menu(team.arr[i])).grid(row=i + 2, column=4)
        else:
            tkinter.Label(frame, text=team.arr[i].start_time).grid(row=i + 2, column=4)
            tkinter.Label(frame, text=team.arr[i].finish_time).grid(row=i + 2, column=5)
            tkinter.Button(frame, text="Изменить время", command=lambda: edit_time_menu(team.arr[i])).grid(row=i + 2, column=6)

    tkinter.Button(frame, command=lambda: edit_menu(Participant()), text="Добавить участника").grid(row=team.arr.__len__() + 2, columnspan=4, stick="we")


def create_window(teams_arr: list, is_end: bool):

    # Создаем главное окно
    root = tkinter.Tk()
    root.minsize(700, 250)
    root.title("Таблицы с названиями команд и списками участников")

    # Здесь должны находиться все фреймы, относящиеся к командам
    mainframe = tkinter.Frame(root)
    mainframe.grid(row=0, column=0)

    for i in range(0, teams_arr.__len__()):
        create_table(teams_arr[i], mainframe, is_end, i // 3, i % 3)

    start_button_frame = tkinter.Frame(root)

    start_button = tkinter.Button(start_button_frame, text="Start", command=lambda: window_rebuild(root, teams_arr))
    start_button_frame.grid(row=1, column=1)
    start_button.pack(padx=50, pady=50)

    # Запускаем главный цикл обработки событий
    root.mainloop()


def create_team(entry_name, entry_something, create_team_menu):
    create_team_menu.destroy()

    team = Team(entry_name.get(), entry_something.get())


def create_team_window():
    create_team_menu = tkinter.Tk()
    create_team_menu.minsize(250, 100)
    create_team_menu.title("Изменение участника команды")

    tkinter.Label(create_team_menu, text="Название команды").grid(row=0, column=0)
    tkinter.Label(create_team_menu, text="Что-то там команды").grid(row=0, column=1)


    create_team_menu.grid_columnconfigure(0, minsize=50)
    create_team_menu.grid_columnconfigure(1, minsize=50)


    entry_name = tkinter.Entry(create_team_menu)
    entry_name.grid(row=1, column=0)
    entry_something = tkinter.Entry(create_team_menu)
    entry_something.grid(row=1, column=1)

    tkinter.Button(create_team_menu, command=lambda: create_team(entry_name, entry_something, create_team_menu), text="Сохранить").grid(row=1, column=2)

def create_first_window():

    # Создаем главное окно
    root = tkinter.Tk()
    root.minsize(700, 250)
    root.title("Таблицы с названиями команд и списками участников")

    # Здесь должны находиться все фреймы, относящиеся к командам
    mainframe = tkinter.Frame(root)
    mainframe.grid(row=0, column=0)


    start_button_frame = tkinter.Frame(root)

    start_button = tkinter.Button(start_button_frame, text="Добавить команду", command=lambda: )
    start_button_frame.grid(row=1, column=1)
    start_button.pack(padx=50, pady=50)

    # Запускаем главный цикл обработки событий
    root.mainloop()

'''
part1 = Participant(1, "Dima", 20, "M")
part2 = Participant(2, "Yana", 21, "Z")

team1 = Team([part1, part2, part1])
team2 = Team([part2, part1])
team3 = Team([part2, part1, part1, part2])
team4 = Team([part2, part1])
team1, team2, team3, team4
'''
teams = []

create_first_window()


