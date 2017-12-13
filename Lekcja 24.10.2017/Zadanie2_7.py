import json

with open('py1.2zd.json') as file:
    data = json.load(file)

sw_ships = open('sw_ships','w', encoding='utf-8')

ships = list()

for item in data:
    if item['cost_in_credits'] == 'unknown':
        cost = -1
    else:
        cost = int(item['cost_in_credits'])

    ships.append([item['name'], cost])

def getKey(item):
    return item[1]

ships.sort(key=getKey,reverse=True)
for item in ships:
    if item[1] == -1:
        cost = '- brak danych'
    else:
        cost = str(item[1])+" credits"

    sw_ships.write(item[0]+" kosztuje "+cost+"\n")

sw_ships.close()