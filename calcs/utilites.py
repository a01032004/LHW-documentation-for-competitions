"""
Содержит в себе вспомогательные функции, используемые для вычислений
"""

import datetime as dt

import config


def get_factor(sex: bool, age: int):
    """Получение коэффициента, на который будет домножатся чистое время

    Args:
        sex (bool): пол участника
        age (int): возвраст участника

    Returns:
        float: коэффициент 
    """
    factors = []
    path = config.man_factor_path if not sex else config.woman_factor_path

    with open(path, "r") as file:
        for row in file.readlines():
            factors.append(list(map(float, row.split())))

    index = -1
    for interval in factors[0]:
        if age - interval < 0:
            index = factors[0].index(interval)
            break

    return factors[1][index]


def total_seconds_to_time(seconds: float):
    """
    Переводит переменную seconds типа float в объект datatime.time
    """
    return dt.time(
        hour=int(seconds) // 3600,
        minute=int(seconds) % 3600 // 60,
        second=int(seconds) % 60
    )


def string_time_to_float(time: str):
    """Перевод строки времени в секунды

    Args:
        time (str): время, представленное в строчке
        следующего формата  (часы, минуты, секунды): "00:00:00" или "00 00 00"

    Returns:
        float: время в секундах
    """
    hour = int(time[0:2]) * 3600
    minute = int(time[3:5]) * 60
    seconds = int(time[6:8])
    return float(hour + minute + seconds)


def get_best_woman(team: list):
    """Находим женщину с наилудшим результатом в команде

    Args:
        team (list): список с участниками команды

    Returns:
        Participant or False: объект Participant, когда в команде есть женщины, иначе False 
    """
    womans = []
    for part in team:
        if part.sex == True:
            womans.append(part)

    if len(womans) == 0:
        return False

    womans.sort(key=lambda part: part.place)

    return womans[0]


def sum_point(team: list, count: int):
    """Подсчитывает бал команды

    Args:
        team (list): список участников команды
        count (int): количество участников, по которым считается бал

    Returns:
        int: командный балл 
    """
    points = 0
    for i in range(0, min(count, len(team))):
        points += team[i].place

    return points
