"""
DocString
:return:
"""

import math
import random
import this

def nic_nie_robie():
    """
    DocString
    :return:
    """
    pi_number = math.pi
    random.randint(0, int(pi_number))
    print(this)


def podzielna(liczba, podzielna_przez):
    """
    DocString
    :return:
    """
    return liczba % podzielna_przez == 0

def ugly(liczba):
    """
    DocString
    :return:
    """
    try:
        if liczba == 1:
            return True
        for i in [2, 3, 5]:
            if podzielna(liczba, i):
                return True
        return False
    except:
        import pdb; pdb.set_trace()
print(ugly((11)))
print(ugly((12)))

def time(czas, jednostka):
    """
    DocString
    :return:
    """
    h, m, s = czas.split(':')
    h = int(h)
    m = int(m)
    s = int(s)
    if jednostka == 's':
        return h * 3600 + m * 60 + s
    elif jednostka == 'm':
        return h * 60 + m + round(s / 60, 2)
    else:
        return h + round(m / 60, 2) + round(s / 3600, 2)

print(time('01:15:59', 's'))
print(time('01:15:59', 'm'))
print(time('01:15:59', 'h'))

RESULT = []
R2 = []

def flatten(arr):
    """
    DocString
    :return:
    """
    for el in arr:
        if isinstance(el, list):
            flatten(el)
        else:
            RESULT.append(el)
    return RESULT

def flatten_nr(arr):
    """
    DocString
    :return:
    """
    while True:
        el = arr.pop()
        if not isinstance(el, list):
            R2.append(el)
        else:
            arr = el
        if not arr:
            break
    return R2[::-1]

print(flatten([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))
print(flatten_nr([[[[[[[[[['a'], 'b']]], 'c']]], 'd']], 'e']))


def weird_power(a):
    """
    DocString
    :return:
    """
    return a ** 2, a ** 3

def calculate(afun, data):
    """
    DocString
    :return:
    """
    return afun(weird_power(data))

A = 3
B = lambda a: sum(a)
C = calculate(B, A)
print(C)

D = lambda a: sorted(a)
F = calculate(D, A)
print(F)


def power_2(a):
    """
    DocString
    :return:
    """
    return (a + 0.5 * a) ** 2

print(power_2(3))

X = lambda a: (a + 0.5 * a) ** 2
print(X(3))


DATA = [(9, 0), (1, 2), (3, 4)]
SORTED_DATA = sorted(DATA, key=lambda a: a[0], reverse=False)
MAX_DATA = max(DATA, key=lambda a: max(a))
MIN_DATA = min(DATA, key=lambda a: max(a))
FILTERED_DATA = list(filter(lambda a: sum(a) > 5, DATA))

print({
    'a': {
        'a': {
            'a': {
                'a': {
                    'a': {
                        'a': {
                            'a': {
                                'a': {
                                    'a': {
                                        'a': {
                                            'a': {
                                                'a': {
                                                    'a': {
                                                        'a': {
                                                            'a': {
                                                                'a': {
                                                                    'a': {
                                                                        'a': {
                                                                            'a': {
                                                                                'a': {
                                                                                    'a': {
                                                                                        'a': {
                                                                                            'a': 1}}}}}}}}}}}}}}}}}}}}}}})
