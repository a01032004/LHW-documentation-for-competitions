

class Participant:
    """

    """

    def __init__(self, _id=-1, name="", starting_number=-1, age=-1, sex="", rank="", group=1, medical_allowance=False):
        self.sex = sex
        self.age = age
        self.name = name
        self.id = _id
        self.rank = rank
        self.group = group
        self.starting_number = starting_number

        self.medical_allowance = medical_allowance
        self.rules_violation_disqualification = False
        self.behaviour_disqualification = False
        self.finish_time = "0:00"
        self.start_time = "0:00"

    def edit_sex(self, sex):
        self.sex = sex

    def edit_age(self, age):
        self.age = age

    def edit_name(self, name):
        self.name = name

    def edit_id(self, _id):
        self.id = _id

    def is_empty(self):
        return self.rank == "" and self.name == "" and self.age == -1 and self.id == -1

    def __eq__(self, other_participant):
        return ((self.age == other_participant.age) and (self.sex == other_participant.sex)
                and (self.id == other_participant.id) and (self.name == other_participant.name))
