file = open('py1.2.txt')

data = file.readlines()
file.close()

file_hero_200_plus = open('hero_200_plus.txt','a')
file_hero_short = open('hero_short.txt','a')

list_200_plus = list()
list_short = list()

for line in data:
    list_tmp = line.split(" has ")
    list_tmp.pop(0)
    list_tmp = list_tmp[0].split(" and is ")
    list_tmp.pop(0)
    list_tmp = list_tmp[0].split(" cm ")
    height = int(list_tmp[0])

    if height > 200:
        list_200_plus.append(line)
    else:
        list_short.append(line)

file_hero_200_plus.writelines(list_200_plus)
file_hero_short.writelines(list_short)

file_hero_200_plus.close()
file_hero_short.close()