from flask import Blueprint, render_template, redirect, request
from ..forms import PokemonForm
from ..models.pokemon import Pokemon
from ..models.db import db
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
    return types


@pokemon.route("", methods=["POST"])
def post_pokemon():
    form = PokemonForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        data = form.data
        new_pokemon = Pokemon(
            number = data["number"],
            attack = data["attack"],
            defense = data["defense"],
            img_url = data["img_url"],
            name = data["name"],
            type = data["type"],
            moves = f"{data['move1']}, {data['move2']}"
        )
        db.session.add(new_pokemon)
        db.session.commit()
        return redirect ("")
    if form.errors:
        print(form.errors)
        return "Bad data"
