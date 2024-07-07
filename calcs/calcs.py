"""
Здесь происходит формирование массива с результатами
"""

import datetime as dt

from calcs.utilites import *
import config

# from classes.Participant import Participant
# from classes.Team import Team


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


    # Корректируем коэффициенты
    for participant in partips:
        participant.factor = get_factor(participant.sex, participant.age)

    # Проходим по partips и вычисляем чистое время и время, домноженное на коэффициент
    for part in partips:
        part_result = []

        part_result.append(part)

        # Высчитываем чистое время
        finish = part.finish_time
        start = part.start_time
        delta = dt.timedelta(hours=finish.hour, minutes=finish.minute, seconds=finish.second) - \
            dt.timedelta(hours=start.hour, minutes=start.minute,
                         seconds=start.second)

        pure_time = total_seconds_to_time(delta.total_seconds())
        part.pure_time = pure_time

        # Высчитываем время, домноженное на коэффициент
        # factor = ut.get_factor(part.sex, part.age)

        factor_time = part.factor * delta.total_seconds()
        result_time = total_seconds_to_time(factor_time)
        part.result_time = result_time

        result.append(part)

    # Сортировка массива по параметру result_time
    result.sort(key=lambda part: part.result_time)

    # Присваиваем места
    for index in range(len(result)):
        result[index].place = index + 1

    return result


def calc_team_competition(teams: list, group: int):
    """Вычисляет место команды в соревнованиях

    Args:
        teams (list): массив, содержащий объекты типа Team
        group (int): группа, по которым проводится подсчёт

    Returns:
        list: массив команд, отсортированных по имени и по очкам
    """

    result = []

    # 4 мужчины и 1 женщица. При отсутствии женщин в команде, по 5 мужчинам
    if group == 1:
        for team in teams:

            # Сортируем список участников команды сначала по полу, а после по месту в личном зачёте
            team.arr.sort(key=lambda part: (part.sex, part.place))

            # Считаем общий бал
            woman = get_best_woman(team.arr)
            if woman:
                team.team_points += sum_point(
                    team.arr, config.number_of_best_parts_in_first_group) + woman.place
            else:
                team.team_points += sum_point(
                    team.arr, config.number_of_best_parts_in_first_group + 1)

            result.append(team)

    # 7 лучших участника
    if group == 2:
        for team in teams:

            # Сортируем список команды сначала по месту
            team.sort(key=lambda part: part.place)

            # Считаем бал
            team.team_points += sum_point(team.arr,
                                             config.number_of_best_parts_in_second_group)

            result.append(team)

    # 3 лучших участника
    if group == 3:
        for team in teams:
            # Сортируем список команды сначала по месту
            team.sort(key=lambda part: part.place)

            # Считаем балл
            team.team_points += sum_point(team.arr,
                                             config.number_of_best_parts_in_third_group)

            result.append(team)

    # Высчитываем место каманд
    result.sort(key=lambda team: team.team_points)
    for index in range(0, len(result)):
        result[index].place = index + 1

    # Сортируем команды по названию, а после по очкам
    result.sort(key=lambda team: (team.team_name, team.team_points))

    return result
