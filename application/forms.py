from flask_wtf import FlaskForm
from wtforms import IntegerField,StringField,SubmitField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError
from application.models import Users, Superheroes

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
	def validate_publisher(self, publisher):
		result = Superheroes.query.filter_by(publisher=publisher.data.upper()).first()
		if not result:
			raise ValidationError('Hero does not exist')
	name=StringField(validators=[Length(max=30)])
	def validate_name(self, name):
		result = Superheroes.query.filter_by(name=name.data.upper()).first()
		if not result:
			raise ValidationError('Hero does not exist')
	alterego=StringField(validators=[Length(max=30)])
	def validate_alterego(self, alterego):
		result = Superheroes.query.filter_by(alterego=alterego.data.upper()).first()
		if not result:
			raise ValidationError('Hero does not exist')
	power=StringField(validators=[Length(max=30)])
	def validate_power(self, power):
		#result = Superheroes.query.filter_by(power=power.data.upper()).first()
		#if not result:
		#	raise ValidationError('Hero does not exist')
	team=StringField(validators=[Length(max=30)])
	def validate_team(self, team):
		result = Superheroes.query.filter_by(team=team.data.upper()).first()
		if not result:
			raise ValidationError('Hero does not exist')
	sidekick=StringField(validators=[Length(max=30)])
	def validate_sidekick(self, sidekick):
		result = Superheroes.query.filter_by(sidekick=sidekick.data.upper()).first()
		if not result:
			raise ValidationError('Hero does not exist')
	nemesis=StringField(validators=[Length(max=30)])
	def validate_nemesis(self, nemesis):
		result = Superheroes.query.filter_by(nemesis=nemesis.data.upper()).first()
		if not result:
			raise ValidationError('Hero does not exist')
	submit=SubmitField('Submit search')
class Delete(FlaskForm):
	confirm=SubmitField('Yes',validators=[DataRequired()])
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