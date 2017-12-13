def BMI(height, mass):
    return round(mass / (height ** 2), 2)

import requests
resp = requests.get(requests.get('https://swapi.co/api/').json()['starships'])

while resp:
    for item in resp.json()['results']:
        if item['name'] == 'Millennium Falcon':
            for pilot_item in item['pilots']:
                height = int(requests.get(pilot_item).json()['height'])/100
                mass = int(requests.get(pilot_item).json()['mass'])
                print("Pilot: {}, BMI: {} ".format(requests.get(pilot_item).json()['name'], str(BMI(height,mass)) ))

    if resp.json()['next'] is not None:
        resp = requests.get(resp.json()['next'])
    else:
        resp = None
