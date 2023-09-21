from flask.cli import AppGroup
from .pokemon import seed_pokemon, undo_pokemon
from .items import seed_items, undo_items
from .pokemon_types import seed_pokemon_types, undo_types

seed_commands = AppGroup("seed")

@seed_commands.command("all")
def seed():
    seed_pokemon()
    seed_items()
    seed_pokemon_types()
    print("In here we will run our seed functions")

@seed_commands.command("undo")
def undo():
    undo_pokemon()
    undo_items()
    undo_types()
    print("In here we will undo everything")
