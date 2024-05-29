

class Participant:
    def __init__(self, sex, age, name, _id):
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
