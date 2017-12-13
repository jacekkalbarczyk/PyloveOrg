file = open('py1.2.txt')

data = file.readlines()
file.close()

dict = {}
for line in data:
    list_tmp = line.split(". ")
    list_tmp.pop(0)
    list_tmp = list_tmp[0].split(" has ")
    name = list_tmp[0]
    list_tmp.pop(0)
    list_tmp = list_tmp[0].split(" and is ")
    eyes = list_tmp[0]
    list_tmp.pop(0)
    list_tmp = list_tmp[0].split(" cm ")
    height = int(list_tmp[0])

    dict[name] = {'height':height, 'eyes':eyes}

print(dict)

#print(data)