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

dict_translation = {}
dict_translation['yellow'] = 'żółty'
dict_translation['black'] = 'czarny'
dict_translation['blue'] = 'niebieski'
dict_translation['orange'] = 'pomarańczowy'
dict_translation['green, yellow'] = 'zielono-żółty'
dict_translation['red'] = 'czerwony'
dict_translation['brown'] = 'brązowy'
dict_translation['unknown'] = 'nieznany'
dict_translation['gold'] = 'złoty'
dict_translation['blue-gray'] = 'niebiesko-szary'
dict_translation['pink'] = 'różowy'
dict_translation['hazel'] = 'piwny'
dict_translation['red, blue'] = 'czerwono-niebieski'

dict_2 = {}

for item in dict:
    eyes = dict[item]['eyes']
    height = dict[item]['height']

    if eyes in dict_2:
        dict_2[eyes]['height_sum'] += height
        dict_2[eyes]['count'] += 1
    else:
        dict_2[eyes] = {'height_sum' : height, 'count': 1}


for item in dict_2:
    print('Średni kolor oczu osób z kolorem oczu '+dict_translation[item]+' wynosi '+str(round(dict_2[item]['height_sum']/dict_2[item]['count'],2))+' cm')
