class Czlowiek:
    def __init__(self, name = "", height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()

    def count_bmi(self):
        return self.weight / (self.height ** 2)

    def diff_to_norm(self):
        if self.bmi < 18.5:
            expected_weight = 18.5*self.height**2
            diff = expected_weight-self.weight
            print("Musisz przytyć {} kg".format(diff))
        elif self.bmi > 25:
            expected_weight = 25*self.height**2
            diff = self.weight- expected_weight
            print("Musisz schudnąć {} kg".format(diff))
        else:
            print("BMI w normie")

Jan = Czlowiek("Jan", 1.9, 65)
Jan.diff_to_norm()


