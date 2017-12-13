import json

with open('py1.2.json') as file:
    data = json.load(file)

sw_women = open('sw_women','w', encoding='utf-8')
sw_men = open('sw_men','w', encoding='utf-8')
for item in data:
    if item['gender'] == 'female':
        sw_women.write(item['name']+"\n")
    elif item['gender'] == 'male':
        sw_men.write(item['name'] + "\n")

sw_women.close()
sw_men.close()

"""
#women = list()
#men = list()

for item in data:
    if item['gender'] == 'female':
        women.append(item['name'])
    elif item['gender'] == 'male':
        men.append(item['name'])


with open('sw_women','w', encoding='utf-8') as file:
    for item in women:
        file.write(item+"\n")

with open('sw_men','w', encoding='utf-8') as file:
    for item in men:
        file.write(item+"\n")"""
