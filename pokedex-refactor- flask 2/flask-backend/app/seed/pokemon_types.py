from app.models import db
from app.models.pokemon_type import Type
from random import choice, sample, randint
from sqlalchemy.sql import text
from faker import Faker
fake = Faker()
from datetime import date



def seed_pokemon_types():

    pokemon1 = Type(
        pokemon_type="fire"
    )

    # all_posts = [post1, post2, post3, post4, post5]
    # add_posts = [db.session.add(post) for post in all_posts]
    db.session.add(pokemon1)
    db.session.commit()



def undo_types():
    db.session.execute(text("DELETE FROM types"))
    # db.session.execute(text("DELETE FROM posts"))
    db.session.commit()
