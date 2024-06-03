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
    path = config.man_factor_path if sex else config.woman_factor_path

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
