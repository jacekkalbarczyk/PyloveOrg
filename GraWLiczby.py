from random import randint

def podaj_liczbe():
    while True:
        try:
            return int(input("Użytkownik: "))
        except ValueError:
            print("!! Niepoprawna Liczba !!")

def porownanie_liczb(liczba_komputera, liczba_uzytkownika):
    wynik = False
    if liczba_komputera == liczba_uzytkownika:
        wynik = True
        print("K: Zgadłeś! Moja liczba to "+str(liczba_komputera))
    elif liczba_komputera < liczba_uzytkownika:
        print("K: Moja liczba jest mniejsza.")
    else:
        print("K: Moja liczba jest większa.")

    return wynik

chce_grac = True
while chce_grac:
    liczba_komputera = randint(1,100)
    licznik = 0
    zgadles = False
    while licznik < 5:
        liczba_uzytkownika = podaj_liczbe()
        if porownanie_liczb(liczba_komputera, liczba_uzytkownika):
            licznik = 5
            zgadles = True
        else:
            licznik += 1

    if not zgadles:
        print("K: Nie zgadłeś, moja liczba to "+str(liczba_komputera)+", może następnym razem !!")

    if input("Czy chcesz grać dalej ?? (T/N)") != 'T':
        chce_grac = False



