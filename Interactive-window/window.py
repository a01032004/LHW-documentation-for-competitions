import tkinter
from classes.Participant import Participant
from classes.Team import Team
from makeExel.makeExel import make1exel
from functools import partial
import calcs.calcs as calc
from calcs.utilites import string_time_to_float
from calcs.utilites import total_seconds_to_time

MAIN_TEAM_ARRAY = [] # ToDo: Что это?


'''
    root: основное окно
    entry_id, entry_name, entry_srtrt_num, entry_age, 
    entry_sex, entry_rank, entry_group, medic, violation, 
    behaviour, entry_start, entry_finish: данные для изменения или добавления участника
    p: Participant,
    team: Team,
    window: передача окна, для его закрытия после удаления,
    is_end: нужна для того, чтобы понимать какое из окон реализовывать.(окно заполнения участников или их времени), 
    is_addition: добавляем участника или изменяем
'''
def apply_changes(root, entry_id, entry_name, entry_srtrt_num, entry_age, entry_sex, entry_rank, entry_group, medic, violation, behaviour, entry_start, entry_finish, p: Participant, team: Team, window, is_end, is_addition):
    if is_addition:# это добавление
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
    else:  # это изменение
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

        if isinstance(entry_start, str) and isinstance(entry_finish, str):
            start_time = string_time_to_float(entry_start)
            finish_time = string_time_to_float(entry_finish)

            start_time = total_seconds_to_time(start_time)
            finish_time = total_seconds_to_time(finish_time)
            p.start_time = start_time
            p.finish_time = finish_time
        else:
            p.start_time = entry_start
            p.finish_time = entry_finish
        window.destroy()
        window_rebuild(root, MAIN_TEAM_ARRAY, is_end)

''''
    открытие нового окна, вероятно, с новым is_end
'''
def window_rebuild(root, teams_arr, is_end):
    root.destroy()
    create_window(teams_arr, is_end)


'''
    окошко изменения времени и дисквалификаций участника
'''
def edit_time_menu(root, participant_to_edit: Participant, team: Team):

    edit_window = tkinter.Toplevel()
    edit_window.minsize(250, 100)
    edit_window.title("Изменение времени участника")
    tkinter.Label(edit_window, text="Снятие за нарушение правил").grid(
        row=0, column=0)
    tkinter.Label(edit_window, text="Снятие за неспортивное поведение").grid(
        row=0, column=1)
    tkinter.Label(edit_window, text='start').grid(row=0, column=2)
    tkinter.Label(edit_window, text="finish").grid(row=0, column=3)
    edit_window.grid_columnconfigure(0, minsize=75)
    edit_window.grid_columnconfigure(1, minsize=75)

    violation = tkinter.BooleanVar()
    entry_violation = tkinter.Checkbutton(
        edit_window, variable=violation, offvalue=False, onvalue=True)
    entry_violation.grid(row=1, column=0)
    behaviour = tkinter.BooleanVar()
    entry_violation = tkinter.Checkbutton(
        edit_window, variable=behaviour, offvalue=False, onvalue=True)
    entry_violation.grid(row=1, column=1)

    entry_start = tkinter.Entry(edit_window)
    entry_start.grid(row=1, column=2)
    entry_finish = tkinter.Entry(edit_window)
    entry_finish.grid(row=1, column=3)

    entry_start.insert(-1, participant_to_edit.start_time)
    entry_finish.insert(-1, participant_to_edit.finish_time)

    # Блок для отображения текущего состояния нажатия чекбаттона
    if participant_to_edit.rules_violation_disqualification:
        violation.set(True)
    else:
        violation.set(False)

    if participant_to_edit.behaviour_disqualification:
        behaviour.set(True)
    else:
        behaviour.set(False)


    tkinter.Button(edit_window, text="Изменить", command=lambda: apply_changes(root, participant_to_edit.id,
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
                                                                               edit_window, True, False)).grid(row=1, column=4)


'''
    окошко изменения имени, возраста и тд участника
'''
def edit_menu(root, team: Team, participant_to_edit: Participant):
    is_addition = True if participant_to_edit == Participant() else False

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

    # установка текущих данных уастника
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
                                                 team, edit_window, False, is_addition), text="Сохранить").grid(row=1, column=8)


'''
    mainframe: фрейм, куда всё пихаем,
    is_end: нужна для того, чтобы понимать какое из окон реализовывать.(окно заполнения участников или их времени)
    frame_row, frame_column: нужны для переноса участников на новую строку, чтобы таблица в экран влезала
'''
def create_table(team: Team, root, mainframe, is_end: bool, frame_row: int, frame_column: int):
    frame = tkinter.Frame(mainframe, padx=5, pady=5)
    frame.grid(row=frame_row, column=frame_column)

    # Генерация шапки
    tkinter.Label(frame, text=team.team_name+" № "+team.team_number).grid(row=0, column=0, columnspan=7 if is_end else 4, stick="we")

    tkinter.Label(frame, text='Id').grid(row=1, column=0)
    tkinter.Label(frame, text="ФИО").grid(row=1, column=1)
    tkinter.Label(frame, text="Стартовый номер").grid(row=1, column=2)
    if is_end:
        tkinter.Label(frame, text="Снятие за нарушение правил").grid(
            row=1, column=3)
        tkinter.Label(frame, text="Снятие за неспортивное поведение").grid(
            row=1, column=4)
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
        tkinter.Label(frame, text=team.arr[i].starting_number).grid(
            row=i + 2, column=2)
        if not is_end:
            tkinter.Button(frame, text="Edit", command=partial(edit_menu, root, team, team.arr[i])).grid(row=i + 2, column=3)
        else:
            tkinter.Label(frame, text=(
                "Да" if team.arr[i].rules_violation_disqualification else "Нет")).grid(row=i + 2, column=3)
            tkinter.Label(frame, text=(
                "Да" if team.arr[i].behaviour_disqualification else "Нет")).grid(row=i + 2, column=4)
            tkinter.Label(frame, text=team.arr[i].start_time).grid(
                row=i + 2, column=5)
            tkinter.Label(frame, text=team.arr[i].finish_time).grid(
                row=i + 2, column=6)
            tkinter.Button(frame, text="Изменить время", command=partial(edit_time_menu, root, team.arr[i], team)).grid(row=i + 2, column=7)

    if not is_end:
        tkinter.Button(frame, command=lambda: edit_menu(root, team, Participant()
                                                        ), text="Добавить участника").grid(row=team.arr.__len__() + 2, columnspan=3, stick="we")

'''
    is_end: нужна для того, чтобы понимать какое из окон реализовывать.(окно заполнения участников или их времени)
'''
def create_window(teams_arr: list, is_end: bool):

    # Создаем главное окно
    root = tkinter.Tk()
    root.minsize(700, 250)
    root.title("Таблицы с названиями команд и списками участников")

    # Здесь должны находиться все фреймы, относящиеся к командам
    mainframe = tkinter.Frame(root)
    mainframe.grid(row=0, column=0)

    # Вывод табличек с командами
    for i in range(0, teams_arr.__len__()): # Вывод таблички с командой
        create_table(teams_arr[i], root, mainframe, is_end, i //
                     3 if not is_end else i, i % 3 if not is_end else 1)

    start_button_frame = tkinter.Frame(root)

    if is_end:
        add_team_button = tkinter.Button(
            start_button_frame, text="Подвести итоги", command=lambda: last_exel_outcome(teams_arr))
    else:
        add_team_button = tkinter.Button(
            start_button_frame, text="Добавить команду", command=lambda: create_team_window(root))
        start_button = tkinter.Button(
            start_button_frame, text="Начать соревнование", command=lambda: window_rebuild_with_exel_outcome(root, teams_arr, True))
    start_button_frame.grid(row=1, column=1)
    add_team_button.pack(padx=50, pady=0)
    
    try:
        start_button.pack(padx=50, pady=5)
    except:
        print("Почини меня! Перепиши window.py! (Если что это около 300-ой строчки:)")
    
    # Запускаем главный цикл обработки событий
    root.mainloop()


def last_exel_outcome(teams_arr):
    make1exel(teams_arr, calc.calc_personal_competition(teams_arr), calc.calc_team_competition(teams_arr, 1), 2)


def window_rebuild_with_exel_outcome(root, teams_arr, is_end):
    make1exel(teams_arr, [], [], 1)
    root.destroy()
    create_window(teams_arr, is_end)


'''
    Функция нужна для добавления команды в глобальный массив команд

    entry_something: номер команды
    create_team_menu: менюшка создания команды. Передаём, чтобы снести
    entry_name: название команды
'''
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

    tkinter.Button(create_team_menu, command=lambda: create_team(
        entry_name, entry_something, create_team_menu), text="Сохранить").grid(row=1, column=2)


def create_first_window():

    # Создаем главное окно
    root = tkinter.Tk()
    root.minsize(700, 250)
    root.title("Таблицы с названиями команд и списками участников")

    # Здесь должны находиться все фреймы, относящиеся к командам
    mainframe = tkinter.Frame(root)
    mainframe.grid(row=0, column=0)

    add_team_button_frame = tkinter.Frame(root)

    add_team_button = tkinter.Button(
        add_team_button_frame, text="Добавить первую команду", command=lambda: create_team_window(root))
    add_team_button_frame.grid(row=1, column=1)
    add_team_button.pack(padx=250, pady=250)

    # Запускаем главный цикл обработки событий
    root.mainloop()

create_first_window()
