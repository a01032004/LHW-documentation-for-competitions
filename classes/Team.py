from classes.Participant import Participant


class Team:
    def __init__(self, participant_arr = []):
        self.arr = participant_arr

    def add_participant(self, participant):
        self.arr.append(participant)

    def delete_participant(self, participant):
        self.arr.remove(participant)

