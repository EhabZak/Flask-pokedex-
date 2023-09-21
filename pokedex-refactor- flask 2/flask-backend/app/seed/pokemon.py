from app.models import db
from app.models.pokemon import Pokemon
from random import choice, sample, randint
from sqlalchemy.sql import text
from faker import Faker
fake = Faker()
from datetime import date



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

    # all_posts = [post1, post2, post3, post4, post5]
    # add_posts = [db.session.add(post) for post in all_posts]
    db.session.add(pokemon1)
    db.session.commit()



def undo_pokemon():
    db.session.execute(text("DELETE FROM pokemon"))
    # db.session.execute(text("DELETE FROM posts"))
    db.session.commit()
