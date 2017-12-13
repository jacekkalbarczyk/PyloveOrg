import requests
resp = requests.get(requests.get('https://swapi.co/api/').json()['planets'])

while resp:
    for item in resp.json()['results']:
        if item['name'] == 'Tatooine':
            for resident in item['residents']:
                print(requests.get(resident).json()['name'])

    if resp.json()['next'] is not None:
        resp = requests.get(resp.json()['next'])
    else:
        resp = None


