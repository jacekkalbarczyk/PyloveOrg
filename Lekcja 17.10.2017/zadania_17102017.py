#zad1.1


"""

def policz_slowa(zdanie):
    return len(zdanie.split(' '))

print('Liczba słów wynosi: '+ str(policz_slowa(input('Podaj zdanie: '))))


można inaczej:

def policz_slowa(zdanie):
    licznik = 0
    zdanie = zdanie.strip()
    for letter in zdanie:
        if letter == ' ':
            licznik += 1

    return licznik+1

print('Liczba słów wynosi: '+ str(policz_slowa(input('Podaj zdanie: '))))"""


#zad1.2
"""
def policz_samogloski(zdanie):
    lista_samoglosek = ['a', 'e', 'i', 'o', 'u', 'y']
    zdanie = zdanie.lower()
    licznik = 0
    for letter in lista_samoglosek:
        licznik += zdanie.count(letter)

    return licznik
print("Liczba samogłosek wynosi: "+ str(policz_samogloski(input("Podaj zdanie: "))))

albo

def policz_samogloski(zdanie):
    lista_samoglosek = ['a', 'e', 'i', 'o', 'u', 'y']
    licznik = 0
    for litera in zdanie.lower():
        if litera in lista_samoglosek:
            licznik += 1

    return licznik
print("Liczba samogłosek wynosi: "+ str(policz_samogloski(input("Podaj zdanie: "))))"""

#zad1.3

"""def xo_checker(input_string):
    x_count = input_string.lower().count('x')
    y_count = input_string.lower().count('y')
    if x_count + y_count != len(input_string):
        return "illegal characters in text"

    return x_count == y_count

print(xo_checker(input("Podaj ciąg znaków: ")))

albo

def xo_checker(input_string):
    x_count = 0
    y_count = 0
    for letter in input_string.lower():
        if letter == 'x':
            x_count += 1
        elif letter == 'o':
            y_count += 1
        else:
            return "illegal characters in text"

    return x_count == y_count

print(xo_checker(input("Podaj ciąg znaków: ")))
"""

#zad1.4
"""
def cenzura_cyfr(ciag_oryginalny):
    ciag_ocenzurowany = ""

    for letter in ciag_oryginalny:
        if letter.isdigit():
            ciag_ocenzurowany += '#'
        else:
            ciag_ocenzurowany += letter

    return ciag_ocenzurowany

print(cenzura_cyfr(input("Podaj ciąg znaków: ")))
"""

#zad 1.6
"""
def odwazniki(A,B):
    nww = A
    while nww % B > 0:
        nww += A

    return nww//A, nww//B

print(odwazniki(int(input('Podaj wagę odważnika A: ')), int(input('Podaj wagę odważnika B: '))))
"""

#zad 1.7
"""
def droga(a, t, v0 = 0):
    return(v0+(a*t**2)/2)


print(droga(float(input('Podaj przyspieszenie: ')), float(input('Podaj czas: ')), float(input('Podaj prędkość początkową: ')) ))
"""

#zad 1.8
""""""
#A = 65
#Z = 90
#a = 97
#z = 122
"""
def cezar(wiadomosc, przesuniecie):
    szyfr = ""
    try:
        int(przesuniecie)
    except ValueError:
        return 'Nieprawidłowa wartość przesunięcia!'

    for litera in wiadomosc:
        if litera.isalpha():
            poczatek = 0
            if litera.isupper():
                poczatek = 65
            else:
                poczatek = 97

            szyfr += chr(((ord(litera)+int(przesuniecie)-poczatek)%26)+poczatek)
        else:
            szyfr += litera

    return szyfr
            
            
            
print(cezar(input("Podaj wiadomość do zaszyfrowania: "), input("Podaj przesunięcie: ")))"""


def cezar(wiadomosc, przesuniecie):
    szyfr = ""
    try:
        int(przesuniecie)
    except ValueError:
        return 'Nieprawidłowa wartość przesunięcia!'

    for litera in wiadomosc:
        if litera.isalpha():
            poczatek = 0
            if litera.isupper():
                poczatek = ord('A')
            else:
                poczatek = ord('a')

            szyfr += chr(((ord(litera) + int(przesuniecie) - poczatek) % 26) + poczatek)
        else:
            szyfr += litera

    return szyfr


print(cezar(input("Podaj wiadomość do zaszyfrowania: "), input("Podaj przesunięcie: ")))

#print(chr(((ord('Z')+Prz-65)%26)+65))
#chr(((ord(litera)+przesuniecie-poczatek)%26)+poczatek)





