from app.models import db
from app.models.pokemon import Pokemon
from sqlalchemy.sql import text

def seed_pokemon():
    pokemon1 = Pokemon(
        number= 1,
        img_url='/images/pokemon_snaps/1.svg',
        name='Bulbasaur',
        attack=49,
        defense=49,
        type='grass',
        moves=[
          'tackle',
          'vine whip'
        ],
        captured=True
    )
    db.session.add(pokemon1)
    db.session.commit()

def undo_pokemon():
    db.session.execute(text("DELETE FROM pokemon"))
    db.session.commit()
