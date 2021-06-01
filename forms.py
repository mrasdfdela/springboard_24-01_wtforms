from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SelectField, StringField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """ Form class for adding pets up for adoption """
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField(
      "Species", 
      choices=[
        ('dog', 'dog'), 
        ('cat', 'cat'), 
        ('porcupine', 'porcupine')], 
      validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age",validators=[Optional(),NumberRange(0,30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """ Form class for editing pet details"""
    photo_url = StringField("Photo URL", validators=[URL(), Optional()])
    age = IntegerField("Age",validators=[Optional(),NumberRange(0,30)])
    notes = StringField("Notes")
    available = BooleanField(
        "available",
        default="checked")
