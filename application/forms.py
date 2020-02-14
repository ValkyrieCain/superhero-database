from flask_wtf import FlaskForm
from wtforms import (IntegerField,StringField,SubmitField)
from wtforms.validators import DataRequired, Length

class FF(FlaskForm):
  id=IntegerField(validators=[DataRequired()])
  name=StringField()
  submit=SubmitField()
class search(FlaskForm):
  search=StringField()
  submitsearch=SubmitField()
