from application import db, login_manager
from flask_login import UserMixin
class Superheroes(db.Model):
	publisher = db.Column(db.String(30))
	name = db.Column(db.String(30))
	alterego = db.Column(db.String(30), primary_key=True)
	p1 = db.Column(db.String(30))
	p2 = db.Column(db.String(30))
	p3 = db.Column(db.String(30))
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
class Users(db.Model,UserMixin):
	id = db.Column(db.Integer, unique=True)
	username = db.Column(db.String(30), primary_key=True)
	password = db.Column(db.String(100), nullable=False)
	def __repr__(self):
		return ''.join(['UserId: ', str(self.id), '\r\n',
			'Username: ', str(self.username), '\r\n',
			'Password: ', self.password])
	@login_manager.user_loader
	def load_user(id):
		return Users.query.get(int(id))