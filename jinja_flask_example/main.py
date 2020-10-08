#!/usr/bin/env python3
import flask
from flask import render_template, request, redirect, url_for

app = flask.Flask("Mitt Zoo")

my_animals = [
    {"name" : "Zebra", "legs" : 4 },
    {"name" : "Elefant", "legs" : 5 },
    {"name": "Blåval", "legs" : 1 },
]

@app.route("/")
def index():
    global my_animals
    search_for = request.args.get("search", "")
    # found = [x for x in my_animals if search_for in x]
    found = []
    for x in my_animals:
        if search_for in x["name"]:
            found.append({
                "name": x["name"],
                "legs" : "x"*x["legs"]
            })
    return render_template("index.html", search=search_for, animals=found)

@app.route("/animal/<int:id>")
def show_animal(id):
    global my_animals
    return render_template("animal.html", animal=my_animals[id])

@app.route("/add", methods=["GET", "POST"])
def add_animal():
    global my_animals
    if "name" in request.form:
        my_animals.append(request.form.get("name"))
        return redirect(url_for("index"))
    return render_template("add_animal.html")


@app.route("/namn", methods=["GET", "POST"])
def namn():
    name = None
    if "name" in request.args:
        name = request.args.get("name")
    if "name" in request.form:
        name = request.form.get("name")
    return render_template("namn.html", name=name)

app.run(debug=True)
