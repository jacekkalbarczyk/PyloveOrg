"""def policz_slowa():
    licznik= 0
    zdanie = input ("podaj zdanie")
    for litera in zdanie.strip():
        if litera == " ":
            licznik +=1
    return licznik +1

print(policz_slowa())"""

def samogloski():
    licznik=0
    zdanie = input("podaj zdanie")
    samgloski = ("a", "e", "i", "o", "u", "y")
    for znak in zdanie.strip():
       if znak in samgloski:
           licznik += 1
    return licznik

print(samogloski())


