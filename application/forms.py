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
class Register(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	passwordagain = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')
class Login(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    def uniqueusername(self, username):
    	user = Users.query.filter_by(username=username.data).first()
    	if user:
    		raise ValidationError('Username not available')