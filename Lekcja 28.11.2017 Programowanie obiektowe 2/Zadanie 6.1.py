class Czas():
    def __init__(self, hour=0, mins=0, sec=0):
        self.hour = hour
        self.mins = mins
        self.sec = sec

czas = Czas(12, 6, 9)
print(czas.hour)
print(czas.mins)
print(czas.sec)
"""class Czas():
    def __init__(self, **kwargs):
        self.hour = kwargs.get('hour')
        self.minutes = kwargs.get('min')
        self.sec = kwargs.get('sec')
        print(self.hour)

k = {'hour' : 9.00, 'mins' : 23 , 'sec' : 12}
f = Czas(**k)"""