from countries import countries

#zad 1.5.1
"""
from countries import countries
print("Państwa z Ameryki Północnej")
for item in countries:
    if(item['subregion'] == 'Northern America'):
        print(item['name']['common'])
"""
#zad 1.5.2
"""
from countries import countries
print("Państwa nie leżące w Afryce")
for item in countries:
    if item['region'] != 'Africa':
        print(item['name']['common'])
"""

#zad 1.5.3
"""
from countries import countries
print("Państwa z wieloma walutami")
for item in countries:
    if len(item['currency']) > 1:
        print(item['name']['common']+"; Lista walut: "+str(item['currency']))
"""

#zad 1.5.4
"""
from countries import countries
from fnmatch import fnmatch
print("Państwa ze stolicami na literę W")
for item in countries:
    if fnmatch(item['capital'],'W*'):
        print(item['name']['common']+"; Stolica: "+item['capital'])
"""

#zad 1.5.5
"""
from countries import countries
print("Największa powierzchnia:")
max_area = 0
country = ""
for item in countries:
    if item['area'] > max_area:
        max_area = item['area']
        country = item['name']['common']

print(country+"; Powierzchnia: "+str(max_area))
"""

#zad 1.5.6
"""
from countries import countries
max_borders = 0
country = ""
for item in countries:
    if len(item['borders']) > max_borders:
        max_borders = len(item['borders'])
        country = item['name']['common']

print(country+"; Liczba granic: "+str(max_borders))
"""




