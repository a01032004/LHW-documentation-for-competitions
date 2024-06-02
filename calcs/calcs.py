"""
Здесь происходит формирование массива с результатами
"""

import datetime as dt


def total_seconds_to_time(seconds):
    """
    Переводит переменную seconds типа float в объект datatime.time
    """
    return dt.datetime(
        hour=int(seconds) //  3600,
        minute=int(seconds) % 3600 // 60,
        second=int(seconds) % 60
    )

arr = []  # Пусть это массив, поступающий на вход

partips = []  # Массив, в котором будут участники соревнований
factor = 0  # Коэффициент будет браться из файла

# Пихаем всех участников в partips
for team in arr:
    for participant in team.participant_arr:
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
    factor_time = factor * delta.total_seconds()
    result_time = total_seconds_to_time(factor_time)
    part_result.append(result_time)
    