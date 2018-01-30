"""
Napisz prosty konwerter walut, który na wejściu przyjmie stringa składającego się z:
kwoty, waluty wejściowej, słówka kluczowego "to" i kwoty wyjściowej.
Użyj następujących kursów: 1 PLN to 1000 USD, 1 PLN to 4505 EURO, 1 PLN to 100 JPY
Załóż, że konwersje są wykonywane tylko z lub do PLNów.
Dla zaawansowanych: przeliczaj wszystkie waluty między sobą (PLN, USD, EURO, JPY)
Przykład:
input: "2 PLN to USD" output: "2000 USD"
input "15 USD to PLN" output: "0.015 PLN"

"""

kurs = {
    'USD': 1000,
    'EURO': 4505,
    'JPY': 100
}

#import pdb; pdb.set_trace()

def convert_currency(currency_string_in = ''):
    value_from, currency_to = currency_string_in.split(' to ')
    value_from, currency_from = value_from.split(' ')
    import pdb; pdb.set_trace()
    pdb.set_trace()

    print(value_from)
    print(currency_from)
    print(currency_to)

convert_currency('2 PLN to USD')

