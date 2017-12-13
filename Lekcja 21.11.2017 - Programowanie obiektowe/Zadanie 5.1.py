#Wyobraźmy sobie klasę "Człowiek" z metodą "mowa" i podklasę "Człowieka" - "Polityk" z metodami "przyjmij łapówkę" i "kłam".
#Domyślnie "Człowiek" po wykonaniu metody "mów" (speak) wypisze "Mowie prawdę",
#natomiast każda instancja "Polityka" powie "Kłamie, bo mogę",
#chyba że wcześniej została wykonana metoda "przyjmij łapówkę" (recive_bribe), wtedy powie prawdę.

class Czlowiek:
    def __init__(self):
        pass

    def speak(self):
        print("Mówię prawdę")

class Polityk(Czlowiek):
    def __init__(self, received_a_bribe = False):
        self.received_a_bribe = received_a_bribe

    def speak(self):
        if self.received_a_bribe:
            super().speak()
        else:
            print("Kłamię, bo mogę")

    def recive_bribe(self):
        self.received_a_bribe = True

Jan_Nowak = Czlowiek()
Jan_Nowak.speak()

Ryszard_Ochodzki = Polityk(True)
Ryszard_Ochodzki.speak()
Ryszard_Ochodzki.recive_bribe()
Ryszard_Ochodzki.speak()
