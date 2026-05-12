from flask import Flask, render_template, redirect, url_for, request, session

from preguntas import get_preguntas, PREGUNTAS


app = Flask(__name__)
app.secret_key = "123"

app.jinja_env.globals["enumerate"] = enumerate

SECCIONES = ["reglas", "evaluacion", "objetivos", "fechas"]

SIGUIENTE = {
    "reglas": "evaluacion",
    "evaluacion": "objetivos",
    "objetivos": "fechas",
    "fechas": None,
}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/seccion/<nombre>")
def seccion(nombre):
    if nombre not in SECCIONES:
        return redirect(url_for("index"))
    indice = SECCIONES.index(nombre)
    if indice > 0 and not session.get(SECCIONES[indice - 1]):
        return redirect(url_for("index"))
    return render_template("seccion.html", seccion=nombre)

@app.route("/preguntas/<nombre>")
def preguntas(nombre):
    if nombre not in SECCIONES:
        return redirect(url_for("index"))

    lista = get_preguntas(nombre)
    return render_template("preguntas.html", seccion=nombre, preguntas=lista, resultado=None)


@app.route("/responder/<nombre>", methods=["POST"])
def responder(nombre):
    if nombre not in SECCIONES:
        return redirect(url_for("index"))

    correctas = 0
    i = 0
    while request.form.get(f"pregunta_{i}"):
        respuesta_correcta = request.form.get(f"pregunta_{i}")
        respuesta_usuario = request.form.get(f"respuesta_{i}")
        if respuesta_usuario == respuesta_correcta:
            correctas += 1
        i += 1

    if correctas == i:
        session[nombre] = True
        return render_template("preguntas.html", seccion=nombre, preguntas=[], resultado="paso", siguiente=SIGUIENTE[nombre])
    else:
        nuevas = get_preguntas(nombre)
        return render_template("preguntas.html", seccion=nombre, preguntas=nuevas, resultado="fallo")
    
if __name__ == "__main__":
    app.run(debug=True)