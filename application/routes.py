from flask import render_template
from application import app
from application import db
from application.models import School
from application.forms import FF, search
@app.route('/')
@app.route('/home')
def home():
 return render_template("home.html")
@app.route('/abc')
def abc():
 return render_template("abc.html", body="hello my friends")
@app.route('/blog', methods=['GET','POST'])
def blog():
 look=search()
 if look.validate_on_submit():
   school=School.query.filter(School.name==look.search.data).all()
   return render_template("blog.html", schooldata=school)
 return render_template("search.html", look=look)
@app.route('/secret')
def secret():
 return render_template("inc.html")
@app.route('/insert', methods=['GET','POST'])
def insert():
 return render_template()
@app.route('/forms', methods=['GET','POST'])
def forms():
 GG=FF()
 if GG.validate_on_submit():
  HI=School(
   id=GG.id.data,
   name=GG.name.data)
  db.session.add(HI)
  db.session.commit()
  print("dancing_man.gif")
 else:
  print("uhoh")
  print(GG.errors)
 return render_template("forms.html", form=GG)
