from flask import Blueprint, render_template, redirect


pokemon = Blueprint("pokemon", __name__)


@pokemon.route("", methods=["GET"])
def index():
    return {"key":"<h1>Practice Assessment</h1>"}
