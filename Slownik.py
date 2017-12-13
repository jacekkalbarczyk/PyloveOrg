"""pusty_slownik = {}
print(pusty_slownik)

slownik = {'a': 'AAAAA', 1:'jeden'}
print(slownik['a'])
print(slownik[1])

slownik['nowy element'] = "NEW"

print(slownik)

slownik['nowy element'] = "____NEW_____"
print(slownik)

del slownik[1]
print(slownik)

if 'a' in slownik:
    print('Jest a')
else:
    print('Ni ma a')"""



slownik_Patryk = {'Imię':'Patryk',
                 'Nazwisko':'Rzepka',
                 'Data urodzenia':'23.02.1983',
                 'Zawód':'Trener futsalu',
                 'Zainteresowania':['Basejumping','Przebieranki'],
                 'Stan konta':1000000
                  }
slownik_Jacek = {'Imię':'Jacek',
                 'Nazwisko':'Kalbarczyk',
                 'Data urodzenia':'29.04.1981',
                 'Zawód':'Kapitan statku wielorybniczego',
                 'Zainteresowania':['Wódka i literatura piękna','Dłubanie w nosie'],
                 'Stan konta':20
                  }
slownik_Baza = {}
# slownik_Baza['Jacek'] = slownik_Jacek.copy() - skopiowanie wartosci bez przypisywania referencji
slownik_Baza['Jacek'] = slownik_Jacek
slownik_Baza['Patryk'] = slownik_Patryk
slownik_Baza['Obaj'] = [slownik_Patryk, slownik_Jacek]

# slownik_Jacek.

# print(slownik_Baza[input("Podaj imię: ")[]])
# print(slownik_Baza)

# print(slownik_Baza['Jacek']['Imię'])
# komu = input("Komu chcesz zdublować stan konta? :")
komu = 'Patryk'
slownik_Baza[komu]['Stan konta'] *= 2
print("Nowy stan konta - "+komu+" "+ str(slownik_Baza[komu]['Stan konta']))

# slownik_Patryk['Zainteresowania'].extend(['Wspinaczka', 'Nurkowanie'])
slownik_Patryk['Zainteresowania']+=['Wspinaczka', 'Nurkowanie']
slownik_Patryk['Nazwisko'] = 'Marciniak'

slownik_Patryk['Drugie imię'] = 'Julian'
slownik_Jacek['Drugie imię'] = 'Marian'

slownik_Patryk['Wiek'] = 34
slownik_Jacek['Wiek'] = 36

slownik_Patryk['Wykształcenie'] = 'Wyższe'
slownik_Jacek['Wykształcenie'] = 'Wyższe'


del slownik_Patryk['Data urodzenia']
del slownik_Jacek['Data urodzenia']

slownik_Patryk['Wiek'] += 5
slownik_Jacek['Wiek'] += 5


print(slownik_Baza[input("Podaj imię: ")])



