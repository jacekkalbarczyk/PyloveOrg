"""pierwszy_sklad = ['Patryk','Lukasz','Górka','Tomek']
print(pierwszy_sklad)
pierwszy_sklad.append('Grzesiek')
print(pierwszy_sklad[-1])"""

"""lista_glowna = [['Anita', 16],['Patryk',34],['Jolka',22]]
lista_imion = list()
lista_imion.append(lista_glowna[0][0])
lista_imion.append(lista_glowna[1][0])
lista_imion.append(lista_glowna[2][0])
lista_wieku = list()
lista_wieku.append(lista_glowna[0][1])
lista_wieku.append(lista_glowna[1][1])
lista_wieku.append(lista_glowna[2][1])

print('Lista imion '+str(lista_imion))
print('Lista wieku '+str(lista_wieku))

# print(str(lista_glowna.pop(0))+"\n"+str(lista_glowna.pop(0))+"\n"+str(lista_glowna.pop(0))) #pop(i) zwraca i usuwa i-ty element, .remove(i) tylko usuwa

print(lista_glowna[0],lista_glowna[1], lista_glowna[2])
"""
"""while len(lista_glowna):
    print(lista_glowna.pop(0))"""


"""print(lista_glowna.pop(0))
print(lista_glowna.pop(0))
print(lista_glowna)"""

"""print(lista_glowna[0])
print(lista_glowna[-2])
print(lista_glowna[2])"""
# help(range(0,100))
"""lista = list(range(100))

print(lista[64:73:2])
print(lista[22::2])
"""
lista_zony = list()
while len(lista_zony) < 3:
    lista_zony.append(input("Żona życzy sobie: "))

lista_kupionych = list()
while len(lista_kupionych) < 3:
    lista_kupionych.append(input("Udało się kupić: "))

lista_nadmiarowa = list()
lista_trafionych = list()

element = ""
while len(lista_kupionych) > 0:
    element = lista_kupionych.pop(0)
    if element in lista_zony:
        lista_trafionych.append(element)
    else:
        lista_nadmiarowa.append(element)

if len(lista_nadmiarowa):
    print('Po cholerę kupiłeś '+str(lista_nadmiarowa)+" ???")
if len(lista_trafionych):
    print('Brawo miśku, kupiłeś '+str(lista_trafionych)+" !")

