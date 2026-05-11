from flask import Flask, render_template, redirect, url_for
from contenido import REGLAS, EVALUACION, OBJETIVOS, FECHAS

app = Flask(__name__)
app.secret_key = "123"

SECCIONES = ["reglas", "evaluacion", "objetivos", "fechas"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/seccion/<nombre>")
def seccion(nombre):
    if nombre not in SECCIONES:
        return redirect(url_for("index"))
    return render_template("seccion.html", seccion=nombre)


if __name__ == "__main__":
    app.run(debug=True)