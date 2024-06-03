"""
Здесь происходит формирование массива с результатами
"""

import datetime as dt

import calcs.utilites as ut

from classes.Participant import Participant
from classes.Team import Team


def calc_personal_competition(arr: list):
    """Вычисляет время, место участников в личном зачёте

    Args:
        arr (list): массив, содержащий объекты типа Team

    Returns:
        list: массив участников, упопядоченных по занятому месту
    """

    result = []
    partips = []  # Массив, в котором будут участники соревнований

    # Пихаем всех участников в partips
    for team in arr:
        for participant in team.arr:
            partips.append(participant)


    # Проходим по partips и вычисляем чистое время и время, домноженное на коэффициент
    for part in partips:
        part_result = []

        part_result.append(part)

        # Высчитываем чистое время
        finish = part.finish_time
        start = part.start_time
        delta = dt.timedelta(
            hours=finish.hour, minutes=finish.minute, seconds=finish.second) - dt.timedelta(
            hours=start.hour, minutes=start.minute, seconds=start.second
        )

        pure_time = ut.total_seconds_to_time(delta.total_seconds())
        part.pure_time = pure_time

        # Высчитываем время, домноженное на коэффициент
        # factor = ut.get_factor(part.sex, part.age)
        
        factor_time = part.factor * delta.total_seconds()
        result_time = ut.total_seconds_to_time(factor_time)
        part.result_time = result_time

        result.append(part)

    # Сортировка массива по параметру result_time
    result.sort(key=lambda part: part.result_time)

    # Присваиваем места
    for index in range(len(result)):
        result[index].place = index + 1

    return result


def calc_team_competition(teams: list):
    """Вычисляет место команды в соревнованиях

    Args:
        teams (list): массив, содержащий объекты типа Team

    Returns:
        list: массив
    """

    result = []

    return result
