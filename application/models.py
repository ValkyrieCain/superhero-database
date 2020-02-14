from application import db

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return ''.join([
            'ID: ', str(self.id), '\n',
            'Name: ', self.name,'\n\n'])
