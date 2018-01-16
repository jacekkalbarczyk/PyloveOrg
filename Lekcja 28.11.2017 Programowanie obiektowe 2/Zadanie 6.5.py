#Zaimplementuj metodę set_time, która pozwoli nadpisać aktualne wartości czasu.

class Czas():
    def __init__(self, hour=0, mins=0, sec=0):
        self.hour = hour
        self.mins = mins
        self.sec = sec

    def set_time(self, hour, mins, sec):
        self.__init__(hour, mins, sec)
        #self.hour = hour
        #self.mins = mins
        #self.sec = sec

    def __str__(self):
       return '<zeg h={}, m={}, s={}>'.format(self.hour, self.mins, self.sec)

cz = Czas(9,10,10)

print(cz.__str__())

cz.set_time(10,22,22)
print(cz.__str__())


"""class Zegar(Czas):
    def __init__(self, format_czasu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_czasu = format_czasu

class DokladnyZegar(Zegar):
    def __init__(self, *args, ms=0, **kwargs):  #WAŻNE: kolejność przekazywania argumentów 1. argumenty pozycyjne
        super().__init__(*args, **kwargs)
        self.ms = ms

    def __str__(self):
        temp = super()
"""