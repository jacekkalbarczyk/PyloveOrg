"""i=1
for letter in 'Ala ma kota':
    print(letter*i)
    i+=1
"""
"""for liczba in range(10,20,2):
    print(liczba)"""


from pprint import pprint as pp

zliczacz = {}
wyraz = input("Podaj wyraz: ")

for let in wyraz:
    if let in zliczacz:
        zliczacz[let] += 1
    else:
        zliczacz[let] = 1
    pp(zliczacz)
pp(zliczacz)





