import datetime as dt

from classes.Participant import Participant


class Team:
    def __init__(self, participant_arr=[], team_name="Команда без названия", team_number=""):
        self.arr = participant_arr
        self.team_name = team_name
        self.team_number = team_number
        
        self.team_points = 0
        self.place = 0

    def add_participant(self, participant):
        self.arr.append(participant)

    def delete_participant(self, participant):
        self.arr.remove(participant)

    def __str__(self):
        string = "Название: " + str(self.team_name) + "; Очки: " + str(self.team_points) + "; Место: " + str(self.place)
        return string