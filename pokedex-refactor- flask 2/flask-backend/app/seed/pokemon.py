from app.models import db
from app.models.pokemon import Pokemon
from sqlalchemy.sql import text
from .images.pokemon_snaps import *

def seed_pokemon():
    pokemon1 = Pokemon(
        number= 1,
        img_url='./images/pokemon_snaps/1.svg',
        name='Bulbasaur',
        attack=49,
        defense=49,
        type_id='grass',
        moves='tackle, whip something',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    db.session.add(pokemon1)
    db.session.commit()

def undo_pokemon():
    db.session.execute(text("DELETE FROM pokemon"))
    db.session.commit()
