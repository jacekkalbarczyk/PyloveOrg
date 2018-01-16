class Czas():
    def __init__(self, hour, mins=0, sec=0):
        self.hour = hour
        self.mins = mins
        self.sec = sec

class Zegar(Czas):
    def __init__(self, format_czasu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_czasu = format_czasu

class DokladnyZegar(Zegar):
    def __init__(self, *args, ms=0, **kwargs):  #WAŻNE: kolejność przekazywania argumentów 1. argumenty pozycyjne 2. argumenty słownikowe
        super().__init__(*args, **kwargs)
        self.ms = ms

zegar = DokladnyZegar('12H', 12, ms=99,  mins = 6, sec = 9)
print(zegar.hour)
print(zegar.mins)
print(zegar.sec)
print(zegar.format_czasu)
print(zegar.ms)