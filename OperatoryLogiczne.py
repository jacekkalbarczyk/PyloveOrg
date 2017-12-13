bok_a = float(input("Podaj 1 bok podstawy: "));
bok_b = float(input("Podaj 2 bok podstawy: "));
bok_h = float(input("Podaj wysokość: "));
objetosc = bok_a*bok_b*bok_h;

"""nie_jest = "jest "
if bok_a!=bok_b:
    nie_jest = "nie jest "

komunikat_kwadrat = 'Podstawa '+nie_jest+'kwadratem';

nie_jest = "jest "
if not bok_a==bok_b==bok_h:
    nie_jest = "nie jest "

komunikat_szescian = 'Prostopadłościan '+nie_jest+'idealnym sześcianem';"""


print("Objętość prostopadłościanu wynosi: "+str(objetosc))
if bok_a==bok_b:
    print("Podstawa jest kwadratem")
    if bok_a==bok_h:
        print("Nie jest sześcianem")
else:
    print("Podstawa nie jest kwadratem")
    print("Nie jest sześcianem")




# print(komunikat_kwadrat)
# print(komunikat_szescian)

