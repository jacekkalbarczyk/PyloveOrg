#Zaimplementuj metodę pozwalającą zwiększyć czas o minutę, sekundę, godzinę,
# a w przypadku Dokładnego Zegara dodatkowo milisekundy.
#  Pamiętaj że przekraczając 60minutę lub sekundę powinna też odpowiednio zwiększyć odpowiednio godzinę lub minutę.
#  Przykład zeg = Zegar(0, 2, 45) zeg.add_time(second=20) print(zeg) >>> <zeg h=0, m=3, s=5>

class Czas():
    def __init__(self, hour=0, mins=0, sec=0):
        self.hour = hour
        self.mins = mins
        self.sec = sec

    def __str__(self):
        temp = "{} ".format(self._get_name())
        for atr in dir(self):
            if not atr.startswith('_') and not callable(getattr(self,atr)):
                temp += "{}={} ".format(atr,getattr(self, atr))
        return temp

    @classmethod
    def _get_name(cls):
        return cls.__name__

    def add_time(self, hour=0, mins=0, sec=0):
        self.hour += hour
        self.mins += mins
        self.sec += sec

        while self.sec > 59:
            self.sec -= 60
            self.mins += 1

        while self.mins > 59:
            self.mins -= 60
            self.hour += 1

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
