"""
Здесь происходит формирование массива с результатами
"""

import datetime as dt

from classes.Participant import Participant
from classes.Team import Team


def total_seconds_to_time(seconds: float):
    """
    Переводит переменную seconds типа float в объект datatime.time
    """
    return dt.time(
        hour=int(seconds) // 3600,
        minute=int(seconds) % 3600 // 60,
        second=int(seconds) % 60
    )


def calc_personal_competition(arr: list):
    """Вычисляет время, место участников в личном зачёте

    Args:
        arr (list): массив, содержащий объекты типа Team

    Returns:
        list: готовый массив, содержащий массивы, которые имеют следующую структуру [Participant, pure_time, factor, result_time, place]
    """

    partips = []  # Массив, в котором будут участники соревнований
    factor = 0.95  # Коэффициент будет браться из файла

    # Пихаем всех участников в partips
    for team in arr:
        for participant in team.arr:
            partips.append(participant)

    # Массив, который будет содержать массивы со следующей структурой: [Participant, pure_time, factor, result_time, place]
    result = []

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

        pure_time = total_seconds_to_time(delta.total_seconds())
        part_result.append(pure_time)

        # Высчитываем время, домноженное на коэффициент
        result.append(factor)
        factor_time = factor * delta.total_seconds()
        result_time = total_seconds_to_time(factor_time)
        part_result.append(result_time)

        result.append(part_result)

    # Сортировка массива по параметру result_time
    result.sort(key=lambda part: part[len(part) - 1])

    # Присваиваем места
    for index in range(len(result)):
        result[index].append(index + 1)

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