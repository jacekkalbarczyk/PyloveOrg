#Zaimplementuj metodę magiczną __str__, która wyświetli aktualne wartości np. <zeg h=0, m=3, s=5>

class Czas():
    def __init__(self, hour=0, mins=0, sec=0):
        self.hour = hour
        self.mins = mins
        self.sec = sec

#    def __str__(self):
#       return '<zeg h={}, m={}, s={}>'.format(self.hour, self.mins, self.sec)
#
    def __str__(self):
        temp = "{} ".format(self._get_name())
        for atr in dir(self):
            if not atr.startswith('_') and not callable(getattr(self,atr)):
                temp += "{}={} ".format(atr,getattr(self, atr))
        return temp

    @classmethod
    def _get_name(cls):
        return cls.__name__



class Zegar(Czas):
    def __init__(self, format_czasu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.format_czasu = format_czasu

class DokladnyZegar(Zegar):
    def __init__(self, *args, ms=0, **kwargs):  #WAŻNE: kolejność przekazywania argumentów 1. argumenty pozycyjne
        super().__init__(*args, **kwargs)
        self.ms = ms

    def __str__(self):
        temp = super()
