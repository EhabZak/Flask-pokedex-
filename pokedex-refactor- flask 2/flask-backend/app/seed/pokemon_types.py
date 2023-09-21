from app.models import db
from app.models.pokemon_type import Type
from sqlalchemy.sql import text

def seed_pokemon_types():
    type1 = Type(
        pokemon_type="fire"
    )
    db.session.add(type1)
    db.session.commit()

def undo_types():
    db.session.execute(text("DELETE FROM types"))
    db.session.commit()
