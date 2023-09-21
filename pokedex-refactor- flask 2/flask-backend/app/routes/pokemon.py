from flask import Blueprint, render_template, redirect, request
from ..forms import PokemonForm
from ..models.pokemon import Pokemon

pokemon = Blueprint("pokemon", __name__)

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

@pokemon.route("", methods=["GET"])
def index():
    all_pokemon = Pokemon.query.all()
    response = [pokemon.to_dict() for pokemon in all_pokemon]
    return response

@pokemon.route("/types", methods=["GET"])
def get_types():
    return {"types": types}


@pokemon.route("", methods=["POST"])
def post_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        return render_template("create_pokemon.html", form=form)
    if form.errors:
        print(form.errors)
        return "Bad data"
