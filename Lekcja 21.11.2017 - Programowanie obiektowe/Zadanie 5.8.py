#Napisz funkcję, która doradzi,
#czy trzeba przytyć czy schudnąć (i ile), wykorzystując poprzednie funkcje (what_to_do).

#list_1 = ['a', 'b', 'c']
#list_2 = ['a', 'b']
#print(set(list_1).intersection(list_2))
"""from collections import Counter
counter1 = Counter('aaaaab').most_common(1)
counter2 = Counter('aaaaab')
print(counter1)
print(counter2.values())
"""
#intersection = counter1 & counter2
#print(intersection.values())
#dict = {'a' : 3, 'b' : 4}
##dict_2 = {'a' : 2, 'b' : 2}
#dict_3 = dict & dict_2
#print(dict_3)

def isLucky(n):
    str_n = str(n)
    sum_1 = 0
    sum_2 = 0
    first_half, second_half = str_n[:len(str_n)//2], str_n[len(str_n)//2:]
    for item in first_half:
        sum_1 += int(item)
    for item in second_half:
        sum_2 += int(item)
    return sum_1==sum_2

print(isLucky(123006))