from app.models import db
from app.models.pokemon_type import Type
from app.models.pokemon import Pokemon
from app.models.item import Item
from app import app
# from random import choice
# from faker import Faker

# fake = Faker()

with app.app_context():
  type1 = Type(
        pokemon_type="fire"
    )
  db.session.add(type1)
  db.session.commit()

  item1 = Item(
        happiness=100,
        img_url="/images/pokemon_berry.svg",
        name="potion",
        price=10,
        pokemon_id=1,
    )

  db.session.add(item1)
  db.session.commit()

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
