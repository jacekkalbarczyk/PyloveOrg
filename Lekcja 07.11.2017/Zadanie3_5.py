import requests
data = requests.get('http://py.net/cat')

with open('cats.jpg','wb')as file:
    file.write(data.content)
print(data)
