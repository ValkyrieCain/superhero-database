from application import db, login_manager
from flask_login import UserMixin
class Superheroes(db.Model):
	publisher = db.Column(db.String(30))
	name = db.Column(db.String(30))
	alterego = db.Column(db.String(30), primary_key=True)
	p1 = db.Column(db.String(30), db.ForeignKey("powers.id"))
	p2 = db.Column(db.String(30), db.ForeignKey("powers.id"))
	p3 = db.Column(db.String(30), db.ForeignKey("powers.id"))
	team = db.Column(db.String(30))
	sidekick = db.Column(db.String(30))
	nemesis = db.Column(db.String(30))
	def __repr__(self):
		return ''.join(['Publisher: ', self.publisher, '\n',
			'Name: ', self.name, '\n',
			'Alter Ego: ', self.alterego, '\n',
			'First Power: ', self.p1, '\n',
			'Second Power: ', self.p2, '\n',
			'Third Power: ', self.p3, '\n',
			'Team: ', self.team, '\n',
			'Sidekick: ', self.sidekick, '\n',
			'Nemesis: ', self.nemesis, '\n'])
class Powers(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	power = db.Column(db.String(30))
	p1 = db.relationship('Superheroes', backref='author', lazy=True)
	p2 = db.relationship('Superheroes', backref='author', lazy=True)
	p3 = db.relationship('Superheroes', backref='author', lazy=True)
class Users(db.Model,UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30), unique=True)
	password = db.Column(db.String(100), nullable=False)
	def __repr__(self):
		return ''.join(['id: ', str(self.id), '\r\n',
			'Username: ', str(self.username), '\r\n',
			'Password: ', self.password])
	@login_manager.user_loader
	def load_user(id):
		return Users.query.get(id)