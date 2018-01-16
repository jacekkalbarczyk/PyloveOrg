"""Napisz aplikację, która po wejściu na adres "/konto" wyświetli stan konta użytkownika i listę ostatnich przelewów.
Początkowy stan konta ustaw np. na 1000 zł.
Na stronie powinien znajdować się formularz, umożliwiający wykonanie przelewu - powinien zawierać dwa pola tekstowe:
* nr konta docelowego,
* kwotę przelewu.
Po przesłaniu formularza kwota na koncie powinna zostać zmniejszona o podaną wartość, ponadto nowy przelew powinien pojawić się na liście ostatnich przelewów.
Upewnij się, że odświeżenie strony po wykonaniu przelewu nie spowoduje wykonania tego przelewu jeszcze raz."""


from flask import Flask, request, render_template, redirect

app = Flask(__name__)



przelewy = []

konto = 1000;

@app.route('/', methods=['GET'])
def przekieruj():
    return redirect('/konto')

@app.route('/konto', methods=['GET', 'POST'])
def dane_przelewu():
    global konto
    if request.method == 'POST':
        konto_docelowe = request.form.get('konto_docelowe')
        kwota = int(request.form.get('kwota'))
        konto -= kwota

        przelewy.append( {'nr_konta': konto_docelowe, 'kwota': kwota})
        return redirect('/konto')

    return render_template('Zad1a.html', stan_konta=konto, przelewy=przelewy)

app.run(debug=True)