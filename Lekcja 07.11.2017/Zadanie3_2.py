import requests
resp = requests.post('http://py.net/register',
    json= {"name": "Mały", "password": "Buddha"}
)
print(resp.json())
