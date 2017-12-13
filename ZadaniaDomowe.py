"""def ugly_numbers( number_tmp ):
    return (number_tmp == 1 or number_tmp%5 == 0 or number_tmp%3 == 0 or number_tmp%2 == 0)

pytanie = True

while pytanie:
    print(ugly_numbers(int(input("Podaj liczbę: "))))
    pytanie = input("Czy chcesz kontynuować?(t/n): ") == 't'
    """


#def get_time(time_str, time_unit):

"""slownik = {'Jacek' : {'Zawód': 'Kosmonauta', 'Nazwisko' : 'Kalbarczyk'},
           'Marian' : {'Zawód': 'Aktor ze spalonego teatru', 'Nazwisko' : 'Opania'}
           }

print(slownik[input('Podaj imię: ')][input('Podaj klucz: ')])
"""

"""def funk(cyfra, zakres):
    if cyfra in range(zakres[0], zakres[1]):
        print("OK")
    else:
        print('{:_>10}'.format('test'))
        #print("Liczba nie znajduje się w zakresie od {}    do    {}".format(*zakres))


zakres = (1,100)

cyfra = int(input('Podaj cyfrę w zakresie {} do {}: ').format(*zakres))

funk(cyfra, zakres)
"""
def flatten(lista,licznik):
    lista_out = list()
    licznik += 1
    for element in lista:
        #print(element)
        #print(len(element))
        if len(element) == 1:
            #print('A'+str(licznik))

            lista_out.append(element)
            #print('c')
            #print(lista_out)

        elif len(element) > 0:
            #print(licznik)
            #print(element)
            for element_2 in flatten(element, licznik):
                lista_out.append(element)

                print(element_2)

    #print(lista_out)
    #print('c')
    return lista_out
    """tmp = list()
    while len(lista) > 0:
        tmp_2 = list()
        tmp_2.append(lista.pop(0))
        if(len(tmp_2[0])>1):
            print('Ho'+str(tmp_2[0]))
            tmp.append(flatten(tmp_2[0]))
        else:
            print('Ha')
            tmp.append(tmp_2[0])
    return tmp"""


lista = [[['a', ['d']], 'c'],'f']#.pop(0)
flatten(lista,-1)
#lista.pop(1)
#print(lista[0][1][1])
#print(flatten(lista,-1))
#flatten(lista)



