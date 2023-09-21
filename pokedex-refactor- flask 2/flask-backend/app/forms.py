from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange, Length


class PokemonForm(FlaskForm):
  number = IntegerField('number', validators=[DataRequired(), NumberRange(min=1)] )
  attack = IntegerField('attack', validators=[DataRequired(), NumberRange(min=1, max=100)])
  defense = IntegerField('defense', validators=[DataRequired(), NumberRange(min=1, max=100)])
  img_url = StringField('img_url', validators=[DataRequired()])
  name = StringField('name', validators=[DataRequired(), Length(min=3, max=255, message="must be between 3 and 255 characters")])
  type = SelectField("type", validators=[DataRequired()])
  moves = StringField('moves', validators=[DataRequired()])
  encounter_rate = FloatField('encounter_rate', validators=[DataRequired(), NumberRange(min=1, max=100)])
  catch_rate = FloatField('catch_rate', validators=[DataRequired(), NumberRange(min=1, max=100)])
  captured = BooleanField('captured', validators=[DataRequired()])


  submit = SubmitField('Submit')
