from application import db
class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return ''.join([
            'ID: ', str(self.id), '\n',
            'Name: ', self.name,'\n'])
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
       	#return ''.join([
        #	'Publisher: ', self.publisher, '\n',
		#	'Name: ', self.name, '\n',
		#	'Alter Ego: ', self.alterego, '\n',
		#	'First Power: ', self.p1, '\n',
		#	'Second Power: ', self.p2, '\n',
		#	'Third Power: ', self.p3, '\n',
		#	'Team: ', self.team, '\n',
		#	'Sidekick: ', self.sidekick, '\n',
		#	'Nemesis: ', self.nemesis, '\n'])
class Users(db.Model):
	username = db.Column(db.String(30), primary_key=True)
	password = db.Column(db.String(100), nullable=False)
	def __repr__(self):
        return ''.join([
        	'UserID: ', str(self.id), '\r\n',
        	'Email: ', self.email])