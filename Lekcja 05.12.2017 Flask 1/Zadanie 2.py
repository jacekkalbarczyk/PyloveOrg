from flask import Flask, request

app = Flask(__name__)

Baobab = "Luj"-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

@app.route("/status", methods=["GET","POST"])
def read():
    global Baobab
    if request.method == 'GET':
        return Baobab
    else:
        data = request.get_json()
        Baobab = data["status"]
        return "Saved status: {}".format(Baobab)

@app.route("/status", methods=["POST"])



app.run(debug=True)

#######

@app.route("/user/<username>/set_password", methods=["POST"])
def set_password(username):
    data = re

