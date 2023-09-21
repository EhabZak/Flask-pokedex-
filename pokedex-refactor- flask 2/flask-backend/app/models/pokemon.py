from .db import db
from datetime import datetime
# from .pokemon_type import types

class Pokemon(db.Model):
    __tablename__ = "pokemons"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    attack = db.Column(db.Integer, nullable=False)
    defense = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False, unique=True)
    # type = db.Column(db.String, nullable=False)
    # type = db.Column(db.Enum(types), nullable=False)
    type_id = db.Column(db.String, db.ForeignKey("types.id"), nullable=False)
    moves = db.Column(db.String(255), nullable=False)
    encounter_rate = db.Column(db.Float, nullable=False, default=1.00)
    catch_rate = db.Column(db.Float, nullable=False, default=1.00)
    captured = db.Column(db.Boolean, nullable=False, default=False)
    # created_at = db.Column(db.DateTime, default=datetime)
    # updated_at = db.Column(db.DateTime, default=datetime)

    # relationship
    item = db.relationship("Item", back_populates = "pokemon")
    type = db.relationship("Type", back_populates = "pokemon")
