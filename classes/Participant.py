

class Participant:
    """

    """
    def __init__(self, sex="M", age=18, name="Prohor", _id=0):
        self.sex = sex
        self.age = age
        self.name = name
        self.id = _id

    def edit_sex(self, sex):
        self.sex = sex

    def edit_age(self, age):
        self.age = age

    def edit_name(self, name):
        self.name = name

    def edit_id(self, _id):
        self.id = _id

    def __eq__(self, other_participant):
        return ((self.age == other_participant.age) and (self.sex == other_participant.sex)
                and (self.id == other_participant.id) and (self.name == other_participant.name))
