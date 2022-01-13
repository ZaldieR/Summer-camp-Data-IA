from flask import Flask
import pandas as pd
from flask import request

df = pd.read_csv('valeursfoncieres-2019.txt', delimiter = "|")
df

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def get_departements():
    departements = df["Code departement"]
    return (departements)

@app.route("/departments")
def departments():
    data = get_departements()
    line = ""
    for i in data:
        line += str(i)
        line += "\n"
    return f"<p>{line}</p>"

def get_postal_code():
    postal = df["Code postal"]
    return postal

@app.route("/postal_codes")
def postal_codes():
    data = get_postal_code()
    line = ""
    for i in data:
        line += str(i)[:-2]
        line += "\n"
    return f"<p>{line}</p>"

def get_departement_housing(departement_id):
    res = []
    data = df[df["Code departement"] == departement_id]
    for i, j, k, l in zip(data['Date mutation'], data['Nature mutation'], data['Valeur fonciere'], \
    data['Surface reelle bati']):
        res.append({'date':i, 'type':j, 'price':k, 'square_meter':l})
    return res

def departements_id():
    print("la")

@app.route("/departments/<int:departement_id>")
def departments_id(departement_id):
    que = request.query_string
    print(que)
    data = get_departement_housing(departement_id)
    line = ""
    for i in data:
        line += str(i)
        line += "\n"
    return f"<p>{line}</p>"


@app.route("/departments/<int:department_id>/postal_codes/<int:postal_code>")
def departments_id_postal(departement_id, postal_code):
    data = get_departements_id(departement_id)
    line = ""
    for i in data:
        line += str(i)
        line += "\n"
    return f"<p>{line}</p>"