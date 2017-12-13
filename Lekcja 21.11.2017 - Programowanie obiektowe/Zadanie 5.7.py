#Zakładając, że aby przytyć 1 kg trzeba dostarczyć 6000kcal, napisz funkcjonalność, która powie użytkownikowi,
#ile powinien zjeść czekolady(450kcal/100g) / ziemniaków(80kcal/100g) więcej aby być w normie (to_eat)

class Czlowiek:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()

    def count_bmi(self):
        return self.weight / (self.height ** 2)

    def to_eat(self):
        if self.bmi < 18.5:
            expected_weight = 18.5*(self.height**2)
            calories_to_gain = (expected_weight-self.weight)*6000
            chocolate = round(calories_to_gain/4500, 2)
            potatoes = round(calories_to_gain/800, 2)
            print('Aby być w normie musisz zjeść {} kg czekolady, lub {} kg ziemniaków'.format(chocolate, potatoes))
        else:
            print('Nie masz niedowagi')

Jan = Czlowiek('Jan', 2, 73)
Jan.to_eat()