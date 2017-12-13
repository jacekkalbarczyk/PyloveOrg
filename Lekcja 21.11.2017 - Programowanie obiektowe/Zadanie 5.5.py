import json

class Czlowiek:
    def __init__(self, name = "", height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = self.count_bmi()
        
    def count_bmi(self):
        return self.weight / (self.height ** 2)

    def save_data(self):
        with open('{}.json'.format(self.name), 'w') as file:
            json.dump(
                {
                    'name' : self.name,
                    'height' : self.height,
                    'weight' : self.weight,
                    'bmi' : round(self.bmi,2)
                },
                file
            )

Jan = Czlowiek('Jan', 1.9, 70)
Jan.save_data()