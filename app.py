from flask import Flask, render_template, redirect, url_for
from contenido import REGLAS, EVALUACION, OBJETIVOS, FECHAS
from preguntas import get_preguntas


app = Flask(__name__)
app.secret_key = "123"

app.jinja_env.globals["enumerate"] = enumerate

SECCIONES = ["reglas", "evaluacion", "objetivos", "fechas"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/seccion/<nombre>")
def seccion(nombre):
    if nombre not in SECCIONES:
        return redirect(url_for("index"))
    datos = {
        "reglas": REGLAS,
        "evaluacion": EVALUACION,
        "objetivos": OBJETIVOS,
        "fechas": FECHAS,
    }
    return render_template("seccion.html", seccion=nombre, datos=datos[nombre])

@app.route("/preguntas/<nombre>")
def preguntas(nombre):
    if nombre not in SECCIONES:
        return redirect(url_for("index"))

    lista = get_preguntas(nombre)
    return render_template("preguntas.html", seccion=nombre, preguntas=lista)


if __name__ == "__main__":
    app.run(debug=True)