class Czlowiek:
    bmi = 0

    def __init__(self, name = "", height = 0, mass = 0):
        self.name = name
        self.height = height
        self.mass = mass

    def count_bmi(self):
        self.bmi = self.mass / (self.height ** 2)

Czlek = Czlowiek("Gruby", 1.7, 120)
print(Czlek.bmi)
Czlek.count_bmi()
print(Czlek.bmi)