from app.models import db
from app.models.pokemon import Pokemon
from sqlalchemy.sql import text
# from .images.pokemon_snaps import *

def seed_pokemon():
    pokemon1 = Pokemon(
        number= 1,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
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
