"""
Napisz aplikacje we flasku, która wygląda jak główna strona google... po kliknięciu szukaj przekierowuje na:
"http://thecatapi.com/api/images/get?format=src&type=gif"
lub na:
"http://thecatapi.com/api/images/get"

"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Z7.html', args)

@app.route("/search", methods=['GET', 'POST'])
def search():
    query = request.args.get('query')
    return render_template('Zadanie 5.html', query=query)

app.run(debug=True)