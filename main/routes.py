from main import app, controller
from flask import render_template


@app.route("/")
def index():
    animals = controller.get_animal_list()
    context = {"animals": animals}
    return render_template("main/index.html", context=context)


@app.route("/animal/<int:animal_id>")
def animal_card(animal_id):
    animal = controller.get_animal()
    context = {"animal": animal}
    return render_template("main/animal.html", context=context)


@app.route("/animal/<int:animal_id>/<procedure>")
def procedure_list(animal_id, procedure):
    procedures = controller.get_procedure_list()
    context = {"procedures": procedures}
    return render_template("main/procedure_list.html", context=context)


@app.route("/animal")
def add_animal():
    return render_template("main/add_animal.html")


@app.route("/add_procedure")
def add_procedure():
    return render_template("main/add_procedure.html")
