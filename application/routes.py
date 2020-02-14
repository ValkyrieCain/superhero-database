from flask import render_template
from application import app
from application import db
from application.models import School
from application.forms import FF
@app.route('/')
@app.route('/home')
def home():
 return render_template("home.html")
@app.route('/abc')
def abc():
 return render_template("abc.html", body="hello my friends")
@app.route('/blog')
def blog():
 school=School.query.all()
 return render_template("blog.html", schooldata=school)
@app.route('/secret')
def secret():
 return render_template("inc.html")
@app.route('/insert', methods=['GET','POST'])
def insert():
 return render_template()
@app.route('/forms')
def forms():
 forms=FF()
 return render_template("forms.html", form=forms, methods=['GET','POST'])
 if form.validate_on_submit():
  formm=form(
   id=form.id.data,
   name=form.name.data)
  db.session.add(formm)
  db.session.commit()
  return redirect(url_for('home'))
 else:
  print("uhoh")
