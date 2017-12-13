from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Bo to Kielce, Kielce, Kielce są, Bracie"

@app.route("/add/<int:num_1>/<int:num_2>")
def add(num_1, num_2):
    return str(num_1+num_2) #str(int(num_1)+int(num_2))

app.run(debug=True)