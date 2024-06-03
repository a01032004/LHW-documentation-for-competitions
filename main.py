from calcs.calcs import calc_personal_competition
from classes.Participant import Participant
from classes.Team import Team
import datetime as dt

if __name__ == "__main__":

    first_part = Participant(1, "First", 12, 26)
    second_part = Participant(2, "Second", 19, 44)
    third_part = Participant(3, "Third", 1, 21)
    fourth_part = Participant(4, "Fourth", 45, 20)

    first_part.start_time = dt.time(12, 0, 0)
    second_part.start_time = dt.time(12, 5, 0)
    third_part.start_time = dt.time(12, 10, 0)
    fourth_part.start_time = dt.time(12, 15, 0)

    first_part.finish_time = dt.time(12, 33, 3)
    second_part.finish_time = dt.time(12, 30, 54)
    third_part.finish_time = dt.time(12, 34, 49)
    fourth_part.finish_time = dt.time(12, 32, 1)

    team_one = Team([first_part, second_part])
    team_two = Team([third_part, fourth_part])

    # Пусть это массив, поступающий на вход
    arr = [team_one, team_two]

    res = calc_personal_competition(arr)
    for part in res:
        print(part)
