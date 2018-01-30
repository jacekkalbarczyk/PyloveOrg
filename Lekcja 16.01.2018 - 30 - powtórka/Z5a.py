"""
Napisz aplikację, która w zależności od argumentu "file" (GET) odczyta plik "hehe.txt",
"heheszki.json" lub "beczka_smiechu.txt" (zawartość dowolna, powinny znajdować się w katalogu z aplikacją).
Obsłuż sytuację, w której plik nie będzie istniał.

"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def load_file():
    filenames = ["hehe.txt", "heheszki.json", "beczka_smiechu.txt"]

    data = request.args
    filename = data.get('file', 'default')

    content = ''
    if filename in filenames:
        try


app.run(debug=True)
