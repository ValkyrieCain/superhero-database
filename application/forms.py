from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from application.models import Users

class Hero(FlaskForm):
	publisher=StringField(validators=[DataRequired(),Length(max=30)])
	name=StringField(validators=[DataRequired(),Length(max=30)])
	alterego=StringField(validators=[DataRequired(),Length(max=30)])
	p1=StringField(validators=[DataRequired(),Length(max=30)])
	p2=StringField(validators=[DataRequired(),Length(max=30)])
	p3=StringField(validators=[DataRequired(),Length(max=30)])
	team=StringField(validators=[DataRequired(),Length(max=30)])
	sidekick=StringField(validators=[Length(max=30)])
	nemesis=StringField(validators=[DataRequired(),Length(max=30)])
	submit=SubmitField('Submit hero')
class Search(FlaskForm):
	publisher=StringField(validators=[Length(max=30)])
	name=StringField(validators=[Length(max=30)])
	alterego=StringField(validators=[Length(max=30)])
	power=StringField(validators=[Length(max=30)])
	team=StringField(validators=[Length(max=30)])
	sidekick=StringField(validators=[Length(max=30)])
	nemesis=StringField(validators=[Length(max=30)])
	submit=SubmitField('Submit search')
	def validate_search(self, alterego):
		result = Superheroes.query.filter(Superheroes.alterego==alterego.data.upper()).first()
		if not result:
			raise ValidationError('Hero does not exist')
class Delete(FlaskForm):
	confirmdelete=SubmitField('Yes',validators=[DataRequired()])
class Register(FlaskForm):
	username = StringField('Username', validators=[DataRequired(),Length(max=30)])
	password = PasswordField('Password', validators=[DataRequired(),Length(max=100)])
	passwordagain = PasswordField('Confirm password', validators=[DataRequired(),Length(max=100),EqualTo('password')])
	submit = SubmitField('Sign Up')
	def validate_username(self, username):
		user = Users.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username not available')
class Login(FlaskForm):
	username = StringField('Username', validators=[DataRequired(),Length(max=30)])
	password = PasswordField('Password', validators=[DataRequired(),Length(max=100)])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')
	def validate_username(self, username):
		user = Users.query.filter_by(username=username.data).first()
		if not user:
			raise ValidationError('Username does not exist')