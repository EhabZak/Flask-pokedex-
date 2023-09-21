from .db import db

# types = [
#   "fire",
#   "electric",
#   "normal",
#   "ghost",
#   "psychic",
#   "water",
#   "bug",
#   "dragon",
#   "grass",
#   "fighting",
#   "ice",
#   "flying",
#   "poison",
#   "ground",
#   "rock",
#   "steel",
# ]

class Type(db.Model):
    __tablename__ = "types"
    id = db.Column(db.Integer, primary_key=True)
    pokemon_type = db.Column(db.String, nullable=False)

    # relationship
    pokemon = db.Relationship("Pokemon", back_populates = "type")
