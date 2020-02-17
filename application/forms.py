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
	sidekick=StringField()
	nemesis=StringField(validators=[DataRequired()])
	submit=SubmitField('Submit new hero')
class Search(FlaskForm):
	publisher=StringField()
	name=StringField()
	alterego=StringField()
	p1=StringField()
	p2=StringField()
	p3=StringField()
	team=StringField()
	sidekick=StringField()
	nemesis=StringField()
	submit=SubmitField('Submit search')