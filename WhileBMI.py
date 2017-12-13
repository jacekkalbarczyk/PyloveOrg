from FunkcjaBMI import oblicz_bmi
def czy_to_jest_cyfra(tekst):
    try:
        float(tekst)
        return tekst
    except ValueError:
        print("ValueError")
        return False

wyjdz = False
while not wyjdz:
    # wzrost = float(czy_to_jest_cyfra(input("Podaj wzrost: ")))
    while
    wzrost = float(czy_to_jest_cyfra(input("Podaj wzrost: ")))
    # czy_to_jest_cyfra(wzrost)
    waga = float(input("Podaj wagę: "))
    # bmi = waga / (wzrost ** 2)
    plec = input("Podaj płeć(K/M): ")
    bmi = oblicz_bmi(wzrost, waga)
    print("Twoje BMI wynosi: " + str(round(bmi, 4)))
    if plec == 'K':
        if(bmi < 20):
            print("Niedowaga")
        elif(bmi <=25):
            print("Norma")
        else:
            print("Nadwaga")
    else:
        if (bmi < 18):
            print("Niedowaga")
        elif (bmi <= 24):
            print("Norma")
        else:
            print("Nadwaga")


    tak_nie = input("Czy chcesz obliczyć BMI dla kolejnej osoby? (T/N): ")
    wyjdz = tak_nie != 'T'