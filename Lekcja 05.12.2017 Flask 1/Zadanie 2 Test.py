import requests

save_result = requests.post(
    'http://localhost:5000/status',
    json={'status': input("Podaj status: ")}
)

#print(save_result.text)

#read_result = requests.get('http://localhost:5000/read')
#print(read_result.text)