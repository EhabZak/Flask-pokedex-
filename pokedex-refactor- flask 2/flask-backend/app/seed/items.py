from app.models import db
from app.models.item import Item
from random import choice, sample, randint
from sqlalchemy.sql import text
from faker import Faker
fake = Faker()
from datetime import date



def seed_items():

    pokemon1 = Item(
        happiness=100,
        img_url="/images/pokemon_berry.svg",
        name="potion",
        price=10,
        pokemon_id=1,
    )

    # all_posts = [post1, post2, post3, post4, post5]
    # add_posts = [db.session.add(post) for post in all_posts]
    db.session.add(pokemon1)
    db.session.commit()



def undo_items():
    db.session.execute(text("DELETE FROM items"))
    # db.session.execute(text("DELETE FROM posts"))
    db.session.commit()
