import requests
resp = requests.get(requests.get('https://swapi.co/api/').json()['species'])

while resp:
    for item in resp.json()['results']:
        if item['name'] == 'Gungan':
            for people_item in item['people']:
                print(list(requests.get(people_item+'?format=wookiee').json().values())[0])

    if resp.json()['next'] is not None:
        resp = requests.get(resp.json()['next'])
    else:
        resp = None