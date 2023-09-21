from .db import db
from datetime import datetime

class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    happiness = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey("pokemons.id"), nullable=False)
    created_at = db.Column(db.Date, default=datetime)
    updated_at = db.Column(db.Date, default=datetime)

    # relationship
    pokemon = db.relationship("Pokemon", back_populates = "item")
