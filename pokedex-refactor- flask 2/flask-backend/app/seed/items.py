from app.models import db
from app.models.item import Item
from sqlalchemy.sql import text

def seed_items():
    item1 = Item(
        happiness=100,
        img_url="/images/pokemon_berry.svg",
        name="potion",
        price=10,
        pokemon_id=1,
    )
    db.session.add(item1)
    db.session.commit()


def undo_items():
    db.session.execute(text("DELETE FROM items"))
    db.session.commit()
