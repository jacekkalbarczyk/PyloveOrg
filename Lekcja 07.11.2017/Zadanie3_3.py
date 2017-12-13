import requests
resp = requests.post('http://py.net/auth',
                     json={
                        "name": "Mały",
                        "password": "Buddha"
                     }
    )
print(resp.json())