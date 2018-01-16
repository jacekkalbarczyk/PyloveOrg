"""
Napisz program, który w zależności od opcji podanej przez użytkownika (1, 2 lub 3)
odczyta odpowiednio plik x.txt, y.txt lub z.txt (zawartość dowolna)
obsługa błędów powinna obejmować (co najmniej) komunikat o nieprawidłowej opcji,
zaś wczytywanie treści pliku powinno znaleźć się w oddzielnej funkcji (wraz z obsługą błędów)

"""
def print_file(option):
    filelist = {1 : 'x.txt', 2 : 'y.txt', 3 : 'z.txt'}
    try:
        filename = filelist[int(option)]
        with open (filename, 'r', encoding='utf-8') as infile:
            print('Zawartość pliku '+filename+':\n'+infile.read())
    except Exception:
        print('Nieprawidłowa opcja.')

print_file(input('Podaj cyfrę 1,2 albo 3: '))