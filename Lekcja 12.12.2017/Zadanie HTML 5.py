from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Zadanie 5.html', nintendo='Kiszot')

@app.route("/search", methods=['GET', 'POST'])
def search():
    query = request.args.get('query')
    return render_template('Zadanie 5.html', query=query)

app.run(debug=True)