from main import app
from flask import render_template


@app.route("/")
def index():
    return render_template("main/index.html")


@app.route("/animal")
def animal():
    return render_template("main/animal.html")


@app.route("/animal/procedure_list")
def procedure_list():
    return render_template("main/procedure_list.html")


@app.route("/add_animal")
def add_animal():
    return render_template("main/add_animal.html")


@app.route("/add_procedure")
def add_procedure():
    return render_template("main/add_procedure.html")
