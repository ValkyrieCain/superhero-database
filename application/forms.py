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
class hero(FlaskForm):
 publisher=StringField((validators=[DataRequired()]))
 name=StringField((validators=[DataRequired()]))
 alterego=StringField((validators=[DataRequired()]))
 p1=StringField((validators=[DataRequired()]))
 p2=StringField((validators=[DataRequired()]))
 p3=StringField((validators=[DataRequired()]))
 team=StringField((validators=[DataRequired()]))
 sidekick=StringField((validators=[DataRequired()]))
 nemesis=StringField((validators=[DataRequired()]))
 submit=SubmitField()
class publisher(FlaskForm):
 publisher=SubmitField('Search by publisher')
class name(FlaskForm):
 name=SubmitField('Search by name')
class alterego(FlaskForm):
 alterego=SubmitField('Search by alter ego')
class power(FlaskForm):
 power=SubmitField('Search by power')
class team(FlaskForm):
 team=SubmitField('Search by team')
class sidekick(FlaskForm):
 sidekick=SubmitField('Search by sidekick')
class nemesis(FlaskForm):
 nemesis=SubmitField('Search by nemesis')