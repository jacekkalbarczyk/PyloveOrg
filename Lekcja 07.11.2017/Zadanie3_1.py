import requests
resp = requests.post(
    'http://py.net/status/set',
    json={
        "status": "Najmojszy status"
    }
)
resp = requests.get('http://py.net/status')
print(resp.json())