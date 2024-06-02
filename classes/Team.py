from classes.Participant import Participant


class Team:
    def __init__(self, participant_arr=[], team_name="Команда без названия", team_something=""):
        self.arr = participant_arr
        self.team_name = team_name
        self.team_something = team_something

    def add_participant(self, participant):
        self.arr.append(participant)

    def delete_participant(self, participant):
        self.arr.remove(participant)

