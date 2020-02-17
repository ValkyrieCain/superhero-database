from flask_wtf import FlaskForm
from wtforms import (IntegerField,StringField,SubmitField)
from wtforms.validators import DataRequired, Length

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
	power=StringField()
	team=StringField()
	sidekick=StringField()
	nemesis=StringField()
	submit=SubmitField('Submit search')