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
    pokemon2 = Pokemon(
        number= 2,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Ivysaur',
        attack=49,
        defense=49,
        type_id='grass',
        moves='tackle, whip it',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon3 = Pokemon(
        number= 3,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Venasaur',
        attack=42,
        defense=29,
        type_id='grass',
        moves='tackle it, whip something',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon4 = Pokemon(
        number= 4,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Charmander',
        attack=4,
        defense=9,
        type_id='fire',
        moves='hot breath',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon5 = Pokemon(
        number= 5,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Charmeleon',
        attack=43,
        defense=4,
        type_id='fire',
        moves='extra hot breath',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon6 = Pokemon(
        number= 6,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Charizard',
        attack=100,
        defense=100,
        type_id='fire',
        moves='stank dragon breath',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon7 = Pokemon(
        number= 7,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Squirtle',
        attack=9,
        defense=9,
        type_id='water',
        moves='waterfall',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon8 = Pokemon(
        number= 8,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Wartortle',
        attack=29,
        defense=29,
        type_id='water',
        moves='tackle',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon9 = Pokemon(
        number= 9,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Blastoise',
        attack=12,
        defense=55,
        type_id='water',
        moves='hydro cannon',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    pokemon10 = Pokemon(
        number= 10,
        img_url='https://i.pinimg.com/originals/0a/b2/92/0ab292cbb44df088d8d8bf97153f7b6c.png',
        name='Pikachu',
        attack=9,
        defense=4,
        type_id='electric',
        moves='thunderbolt',
        # encounter_rate=1.00,
        # catch_rate=1.00,
        captured=True
    )
    all_pokemon = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7, pokemon8, pokemon9, pokemon10]
    add_pokemon = [db.session.add(pokemon) for pokemon in all_pokemon]
    db.session.commit()

def undo_pokemon():
    db.session.execute(text("DELETE FROM pokemon"))
    db.session.commit()
