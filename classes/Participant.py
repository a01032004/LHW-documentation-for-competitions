import datetime

from calcs.utilites import get_factor


class Participant:

    def __init__(  # Зачем id и starting_number, если можно сортировать в лексико-графическом порядке?
        self, _id=-1, name="", starting_number=-1, age=18,
        sex="м", rank="", group=1, medical_allowance=False
    ):
        # False подразумевает мужской пол
        self.sex = False if sex.upper() == "М" else True
        self.age = age
        self.name = name
        self.id = _id
        self.rank = rank
        self.group = group
        self.starting_number = starting_number

        self.medical_allowance = medical_allowance
        self.rules_violation_disqualification = False
        self.behaviour_disqualification = False
        self.doctor_removed = False # Показывает, был ли удалён медицинским работником по состоянию здоровья
        self.finish_time = datetime.time()
        self.start_time = datetime.time()

        # Поля, заполняемые в модуле calcs
        self.pure_time = datetime.time()
        self.result_time = datetime.time()
        self.place = -1

        # Высчитывается коэффициент, на который должно домножиться время
        self.factor = get_factor(self.sex, self.age)

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

    def __str__(self):
        string = "Номер: " + str(self.starting_number) + "; Имя: " + self.name + "; Возраст: " + str(self.age)
        string += "; Результат: " + str(self.result_time)
        string += "; Место: " + str(self.place)
        return string

    def __eq__(self, other_participant):
        return ((self.age == other_participant.age) and (self.sex == other_participant.sex)
                and (self.id == other_participant.id) and (self.name == other_participant.name))
