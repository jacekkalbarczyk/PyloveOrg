from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def hello():
    name = request.args.get('name')
    name2 = request.args.get('name2')
    return render_template('Zadanie 3.html', name=name, name2=name2)

app.run(debug=True)