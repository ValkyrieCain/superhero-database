from flask_wtf import FlaskForm
from wtforms import (IntegerField,StringField,SubmitField)
from wtforms.validators import DataRequired, Length

class FF(FlaskForm):
 id=IntegerField(validators=[DataRequired()])
 name=StringField()
 submit=SubmitField()
class Sch(FlaskForm):
 search=StringField()
 submitsearch=SubmitField()
class Hero(FlaskForm):
 publisher=StringField(validators=[DataRequired()])
 name=StringField(validators=[DataRequired()])
 alterego=StringField(validators=[DataRequired()])
 p1=StringField(validators=[DataRequired()])
 p2=StringField(validators=[DataRequired()])
 p3=StringField(validators=[DataRequired()])
 team=StringField(validators=[DataRequired()])
 sidekick=StringField(validators=[DataRequired()])
 nemesis=StringField(validators=[DataRequired()])
 submit=SubmitField('Submit')