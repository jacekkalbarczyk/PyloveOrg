# wzrost = float(input("Podaj wzrost: "))
# waga = float(input("Podaj wagę: "))
# bmi(wzrost, waga)

# def moje_dzialanie(a,b,dzialanie = '+'):
#     wynik = ""
#     if(dzialanie == '+'):
#         wynik = str(a+b)
#     elif(dzialanie == '-'):
#         wynik = str(a-b)
#     elif(dzialanie == '*'):
#         wynik = str(a*b)
#     elif(dzialanie == '/'):
#         wynik = str(a/b)
#     elif (dzialanie == '**'):
#         wynik = str(a**b)
#
#     if len(wynik):
#         print("Wynik dzialania "+dzialanie+" = "+wynik)
#     else:
#         print("Błędne działanie")
#
# a = float(input("Podaj a: "))
# b = float(input("Podaj b: "))
# dzialanie = input("Podaj działanie(+,-,*,/,**): ")
#
# moje_dzialanie(a,b,dzialanie)

def obliczObjetoscProstopadloscianu(a,b,h):
    return a*b*h

a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
h = float(input("Podaj h: "))
print("V wynosi: "+str(obliczObjetoscProstopadloscianu(a, b, h)))





