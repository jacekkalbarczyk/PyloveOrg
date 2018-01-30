"""
Napisz aplikację - na podstawie podanego szablonu - która po podaniu tekstu i liczby zwróci tekst "przesunięty w prawo"
(uwaga: ograniczamy się do małych liter alfabetu łacińskiego) o liczbę podaną przez użytkownika (np. abcd -> bcde, zdcb -> aedc)
Przydatne funkcje: chr, ord
Przydatny operator: % (modulo)
Przydatna informacja: alfabet łaciński ma 26 liter

"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def cezar_encrypt():
    content = 'Kontent'

    return render_template('Cezar.html', encrypted_text=content)

app.run(debug=True)
