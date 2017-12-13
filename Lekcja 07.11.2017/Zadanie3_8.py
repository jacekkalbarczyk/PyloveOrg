import requests
resp = requests.get(requests.get('https://swapi.co/api/').json()['films'])

while resp:
    for item in resp.json()['results']:
        if item['title'] == 'The Empire Strikes Back':
            for species_item in item['species']:
                print(requests.get(species_item).json()['name'])

    if resp.json()['next'] is not None:
        resp = requests.get(resp.json()['next'])
    else:
        resp = None