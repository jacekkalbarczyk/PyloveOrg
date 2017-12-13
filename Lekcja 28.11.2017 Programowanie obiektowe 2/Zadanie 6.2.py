class Czas():
    def __init__(self, hour, mins=0, sec=0):
        self.hour = hour
        self.mins = mins
        self.sec = sec

class Zegar(Czas):
    def __init__(self, format_czasu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_czasu = format_czasu


zegar = Zegar('12H', 12, mins = 6, sec = 9)
print(zegar.hour)
print(zegar.mins)
print(zegar.sec)
print(zegar.format_czasu)