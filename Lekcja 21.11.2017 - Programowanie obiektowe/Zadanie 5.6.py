#Zakładając, że aby schudnąć 1 kg trzeba spalić 6000kcal,
#napisz funkcjonalność, która powie użytkownikowi,
#ile powinien godzin biegać(500kcal/h) / jeździć rowerem(600kcal/h) / uprawiać hobby(250kcal/h) / grać w szachy(150kcal/h) /
#etc. aby być w normie (to_burn).

class Czlowiek:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()

    def count_bmi(self):
        return self.weight / (self.height ** 2)

    def to_burn(self):
        if self.bmi > 25:
            expected_weight = 25*(self.height**2)
            calories_to_burn = (self.weight-expected_weight)*6000
            run_time = round(calories_to_burn/500, 2)
            bike_time = round(calories_to_burn/600, 2)
            hobby_time = round(calories_to_burn/250, 2)
            chess_time = round(calories_to_burn/150, 2)
            print('Aby być w normie musisz biegać przez {}, jeździć na rowerze przez {}, uprawiać hobby przez {} lub grać w szachy przez {} godzin.'
                  .format(run_time, bike_time, hobby_time, chess_time))
        else:
            print('Nie masz nadwagi')

Jan = Czlowiek('Jan', 2, 101)
Jan.to_burn()