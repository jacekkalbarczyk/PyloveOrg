"""
Napisz algorytm, który na wejście przyjmie listę zawierającą tylko stringi i integery.
Zwróci listą zawierającą tylko powtarzające się wartości, nie zmieniając ich kolejności.
Przykład: [1, 2, 3, 1, 3] 1 i 3 nie są unikalne, więc wynikiem będzie [1, 3, 1, 3].

"""

def non_unique_list(list_in = []):
    list_out =[]
    for element in list_in:
        if list_in.count(element) > 1:
            list_out.append(element)

    return list_out


assert non_unique_list([1,2,3,1,3]) == [1,3,1,3]

#lista = [1,2,3,1,3]
#print(non_unique_list(lista))

