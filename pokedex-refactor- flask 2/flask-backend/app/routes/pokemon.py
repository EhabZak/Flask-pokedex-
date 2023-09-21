from flask import Blueprint, render_template, redirect, request
from ..forms import PokemonForm

pokemon = Blueprint("pokemon", __name__)


@pokemon.route("", methods=["GET"])
def index():
    return {"key":"<h1>Practice Assessment</h1>"}


@pokemon.route("", methods=["POST"])
def post_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        return render_template("create_pokemon.html", form=form)
    if form.errors:
        print(form.errors)
        return "Bad data"
