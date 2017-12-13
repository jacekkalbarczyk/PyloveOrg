import json

with open('py1.2.json') as file:
    data = json.load(file)

sw_all_heroes = open('sw_all_heroes','w', encoding='utf-8')

dict_plec = {
    'male':'jest mężczyzną',
    'female':'jest kobietą',
    'n/a':'jest nieznanej płci',
    'hermaphrodite':'jest hermafrodytą',
    'none':'nie posiada płci'
}

for item in data:
    mass = item['mass']
    if mass == 'unknown':
        mass = ', waga - nieznana,'
    else:
        mass = ' waży '+mass+' kg,'

    planet = item['homeworld']
    if planet == 'unknown':
        planet = ', pochodzenie - nieznane'
    else:
        planet = 'i pochodzi z '+planet

    sw_all_heroes.write(item['name']+mass+" "+dict_plec[item['gender']]+" "+planet+"\n")

sw_all_heroes.close()
