from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

class PokemonForm(FlaskForm):
  number = IntegerField('number', validators=[DataRequired(), NumberRange(min=1)] )
  attack = IntegerField('attack', validators=[DataRequired(), NumberRange(min=1, max=100)])
  defense = IntegerField('defense', validators=[DataRequired(), NumberRange(min=1, max=100)])
  img_url = StringField('img_url', validators=[DataRequired()])
  name = StringField('name', validators=[DataRequired(), Length(min=3, max=255, message="must be between 3 and 255 characters")])
  type = SelectField("type", validators=[DataRequired()], choices=types)
  move1 = StringField('move1', validators=[DataRequired()])
  move2 = StringField('move2', validators=[DataRequired()])
  submit = SubmitField('Submit')
