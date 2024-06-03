import tkinter
from classes.Participant import Participant
from classes.Team import Team

MAIN_TEAM_ARRAY = []


# В этой функции будет происходить изменение данных в эксель, и, как я понимаю, снос имеющейся таблицы и создание новой с измененными данными
def apply_changes(root, entry_id, entry_name, entry_srtrt_num, entry_age, entry_sex, entry_rank, entry_group, medic, violation, behaviour, entry_start, entry_finish, p: Participant, team: Team, window, is_end):
    if p.is_empty():# это добавление
        p.id = entry_id
        p.name = entry_name
        p.starting_number = entry_srtrt_num
        p.age = entry_age
        p.sex = entry_sex
        p.rank = entry_rank
        p.group = entry_group
        p.medical_allowance = medic
        p.rules_violation_disqualification = violation
        p.behaviour_disqualification = behaviour
        p.start_time = entry_start
        p.finish_time = entry_finish
        team.add_participant(p)
        window.destroy()
        window_rebuild(root, MAIN_TEAM_ARRAY, is_end)
    else:# это изменение
        p.id = entry_id
        p.name = entry_name
        p.starting_number = entry_srtrt_num
        p.age = entry_age
        p.sex = entry_sex
        p.rank = entry_rank
        p.group = entry_group
        p.medical_allowance = medic
        p.rules_violation_disqualification = violation
        p.behaviour_disqualification = behaviour
        p.start_time = entry_start
        p.finish_time = entry_finish
        window.destroy()
        window_rebuild(root, MAIN_TEAM_ARRAY, is_end)


def window_rebuild(root, teams_arr, is_end):
    root.destroy()
    create_window(teams_arr, is_end)


def edit_time_menu(root, participant_to_edit: Participant, team: Team):
    edit_window = tkinter.Toplevel()
    edit_window.minsize(250, 100)
    edit_window.title("Изменение времени участника")
    tkinter.Label(edit_window, text="Снятие за нарушение правил").grid(row=0, column=0)
    tkinter.Label(edit_window, text="Снятие за неспортивное поведение").grid(row=0, column=1)
    tkinter.Label(edit_window, text='start').grid(row=0, column=2)
    tkinter.Label(edit_window, text="finish").grid(row=0, column=3)
    edit_window.grid_columnconfigure(0, minsize=75)
    edit_window.grid_columnconfigure(1, minsize=75)

    violation = tkinter.BooleanVar()
    entry_violation = tkinter.Checkbutton(edit_window, variable=violation, offvalue=False, onvalue=True)
    entry_violation.grid(row=1, column=0)
    behaviour = tkinter.BooleanVar()
    entry_violation = tkinter.Checkbutton(edit_window, variable=behaviour, offvalue=False, onvalue=True)
    entry_violation.grid(row=1, column=1)
    

    entry_start = tkinter.Entry(edit_window)
    entry_start.grid(row=1, column=2)
    entry_finish = tkinter.Entry(edit_window)
    entry_finish.grid(row=1, column=3)

    entry_start.insert(-1, participant_to_edit.start_time)
    entry_finish.insert(-1, participant_to_edit.finish_time)
    if participant_to_edit.rules_violation_disqualification:
        violation.set(True)
    else:
        violation.set(False)

    if participant_to_edit.behaviour_disqualification:
        behaviour.set(True)
    else:
        behaviour.set(False)

    tkinter.Button(edit_window, text="Сохранить", command=lambda: apply_changes(root, participant_to_edit.id,
                                                                               participant_to_edit.name,
                                                                               participant_to_edit.starting_number,
                                                                               participant_to_edit.age,
                                                                               participant_to_edit.sex,
                                                                               participant_to_edit.rank,
                                                                               participant_to_edit.group,
                                                                               participant_to_edit.medical_allowance,
                                                                               violation.get(), behaviour.get(),
                                                                                entry_start.get(), entry_finish.get(),
                                                                               participant_to_edit, team,
                                                                               edit_window, True)).grid(row=1, column=4)


def edit_menu(root, team: Team, participant_to_edit: Participant):

    edit_window = tkinter.Toplevel()
    edit_window.minsize(250, 100)
    edit_window.title("Изменение участника команды")

    tkinter.Label(edit_window, text='Id').grid(row=0, column=0)
    tkinter.Label(edit_window, text="ФИО").grid(row=0, column=1)
    tkinter.Label(edit_window, text="Стартовый номер").grid(row=0, column=2)
    tkinter.Label(edit_window, text="Возраст").grid(row=0, column=3)
    tkinter.Label(edit_window, text="Пол").grid(row=0, column=4)
    tkinter.Label(edit_window, text="Звание").grid(row=0, column=5)
    tkinter.Label(edit_window, text="Группа").grid(row=0, column=6)
    tkinter.Label(edit_window, text="Допущен врачем").grid(row=0, column=7)

    edit_window.grid_columnconfigure(0, minsize=50)
    edit_window.grid_columnconfigure(1, minsize=50)
    edit_window.grid_columnconfigure(2, minsize=50)
    edit_window.grid_columnconfigure(3, minsize=50)
    edit_window.grid_columnconfigure(4, minsize=50)

    entry_id = tkinter.Entry(edit_window)
    entry_id.grid(row=1, column=0)
    entry_name = tkinter.Entry(edit_window)
    entry_name.grid(row=1, column=1)

    entry_strt_num = tkinter.Entry(edit_window)
    entry_strt_num.grid(row=1, column=2)

    entry_age = tkinter.Entry(edit_window)
    entry_age.grid(row=1, column=3)

    entry_sex = tkinter.Entry(edit_window)
    entry_sex.grid(row=1, column=4)

    entry_rank = tkinter.Entry(edit_window)
    entry_rank.grid(row=1, column=5)

    entry_group = tkinter.Entry(edit_window)
    entry_group.grid(row=1, column=6)

    medic_var = tkinter.BooleanVar()
    entry_medic = tkinter.Checkbutton(edit_window, variable=medic_var,
                                      offvalue=False, onvalue=True)

    entry_medic.grid(row=1, column=7)

    if participant_to_edit.id != -1:
        entry_id.insert(-1, participant_to_edit.id)
    entry_name.insert(-1, participant_to_edit.name)
    if participant_to_edit.age != -1:
        entry_age.insert(-1, participant_to_edit.age)
    entry_sex.insert(-1, participant_to_edit.sex)
    entry_strt_num.insert(-1, participant_to_edit.starting_number)
    entry_rank.insert(-1, participant_to_edit.rank)
    entry_group.insert(-1, participant_to_edit.group)

    if participant_to_edit.medical_allowance:
        medic_var.set(True)
    else:
        medic_var.set(False)

    tkinter.Button(edit_window,
                   command=lambda: apply_changes(root, entry_id.get(), entry_name.get(), entry_strt_num.get(),
                                                 entry_age.get(), entry_sex.get(),
                                                 entry_rank.get(), entry_group.get(), medic_var.get(),
                                                 participant_to_edit.rules_violation_disqualification,
                                                 participant_to_edit.behaviour_disqualification,
                                                 participant_to_edit.start_time, participant_to_edit.finish_time,
                                                 participant_to_edit,
                                                 team, edit_window, False), text="Сохранить").grid(row=1, column=8)


# Создаем функцию для создания таблицы
def create_table(team: Team, root, mainframe, is_end: bool, frame_row: int, frame_column: int):
    frame = tkinter.Frame(mainframe, padx=5, pady=5)
    frame.grid(row=frame_row, column=frame_column)

    # Генерация шапки
    tkinter.Label(frame, text=team.team_name+" № "+team.team_number).grid(row=0, column=0, columnspan=7 if is_end else 4, stick="we")
    tkinter.Label(frame, text='Id').grid(row=1, column=0)
    tkinter.Label(frame, text="ФИО").grid(row=1, column=1)
    tkinter.Label(frame, text="Стартовый номер").grid(row=1, column=2)
    if is_end:
        tkinter.Label(frame, text="Снятие за нарушение правил").grid(row=1, column=3)
        tkinter.Label(frame, text="Снятие за неспортивное поведение").grid(row=1, column=4)
        tkinter.Label(frame, text="Время старта").grid(row=1, column=5)
        tkinter.Label(frame, text="Время финиша").grid(row=1, column=6)

    frame.grid_columnconfigure(0, minsize=50)
    frame.grid_columnconfigure(1, minsize=50)
    frame.grid_columnconfigure(2, minsize=50)
    frame.grid_columnconfigure(3, minsize=50)
    frame.grid_columnconfigure(4, minsize=50)

    # Вывод участников команды
    for i in range(0, team.arr.__len__()):
        tkinter.Label(frame, text=team.arr[i].id).grid(row=i + 2, column=0)
        tkinter.Label(frame, text=team.arr[i].name).grid(row=i + 2, column=1)
        tkinter.Label(frame, text=team.arr[i].starting_number).grid(row=i + 2, column=2)
        if not is_end:
            tkinter.Button(frame, text="Edit", command=lambda: edit_menu(root, team, team.arr[i])).grid(row=i + 2, column=3)
        else:
            tkinter.Label(frame, text=("Да" if team.arr[i].rules_violation_disqualification else "Нет")).grid(row=i + 2, column=3)
            tkinter.Label(frame, text=("Да" if team.arr[i].behaviour_disqualification else "Нет")).grid(row=i + 2, column=4)
            tkinter.Label(frame, text=team.arr[i].start_time).grid(row=i + 2, column=5)
            tkinter.Label(frame, text=team.arr[i].finish_time).grid(row=i + 2, column=6)
            tkinter.Button(frame, text="Изменить время", command=lambda: edit_time_menu(root, team.arr[i], team)).grid(row=i + 2, column=7)

    if not is_end:
        tkinter.Button(frame, command=lambda: edit_menu(root, team, Participant()), text="Добавить участника").grid(row=team.arr.__len__() + 2, columnspan=3, stick="we")


def create_window(teams_arr: list, is_end: bool):

    # Создаем главное окно
    root = tkinter.Tk()
    root.minsize(700, 250)
    root.title("Таблицы с названиями команд и списками участников")

    # Здесь должны находиться все фреймы, относящиеся к командам
    mainframe = tkinter.Frame(root)
    mainframe.grid(row=0, column=0)

    for i in range(0, teams_arr.__len__()):
        create_table(teams_arr[i], root, mainframe, is_end, i // 3 if not is_end else i, i % 3 if not is_end else 1)

    start_button_frame = tkinter.Frame(root)

    if is_end: # Здесь вызов функции Айдара вместо create_team_window
        add_team_button = tkinter.Button(start_button_frame, text="Подвести итоги", command=lambda: create_team_window(root))
    else:
        add_team_button = tkinter.Button(start_button_frame, text="Добавить команду", command=lambda: create_team_window(root))
    start_button = tkinter.Button(start_button_frame, text="Start", command=lambda: window_rebuild(root, teams_arr, True))
    start_button_frame.grid(row=1, column=1)
    add_team_button.pack(padx=50, pady=0)
    start_button.pack(padx=50, pady=5)

    # Запускаем главный цикл обработки событий
    root.mainloop()


def create_team(entry_name, entry_something, create_team_menu):
    team = Team([], entry_name.get(), entry_something.get())
    global MAIN_TEAM_ARRAY
    MAIN_TEAM_ARRAY.append(team)
    create_team_menu.destroy()
    create_window(MAIN_TEAM_ARRAY, False)


def create_team_window(root):
    root.destroy()
    create_team_menu = tkinter.Tk()
    create_team_menu.minsize(250, 100)
    create_team_menu.title("Изменение участника команды")

    tkinter.Label(create_team_menu, text="Название команды").grid(row=0, column=0)
    tkinter.Label(create_team_menu, text="Номер команды").grid(row=0, column=1)


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


    add_team_button_frame = tkinter.Frame(root)

    add_team_button = tkinter.Button(add_team_button_frame, text="Добавить первую команду", command=lambda: create_team_window(root))
    add_team_button_frame.grid(row=1, column=1)
    add_team_button.pack(padx=250, pady=250)

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


