import requests
resp = requests.post('http://py.net/auth',
                     json={
                        "name": "Mały",
                        "password": "Buddha"
                     }
    )

api_key = resp.json()["api_key"]
resp = requests.post('http://py.net/user_status/set',
                     json={
                        "api_key": api_key,
                        "status": "Jestem liściem na spokojnej tafli jeziora"
                     }
    )
resp = requests.get('http://py.net/user_status')
print(resp.json())
#print(resp.json()["Nazwa kolegi obok"])