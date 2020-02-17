from flask import render_template, redirect
from application import app
from application import db 
from application.models import School, Superheroes
from application.forms import FF, Sch, Hero
@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html")
@app.route('/abc')
def abc():
  return render_template("abc.html", body="hello my friends")
@app.route('/blog', methods=['GET','POST'])
def blog():
  school=School.query.all()
  return render_template("blog.html", schooldata=school)
@app.route('/secret')
def secret():
  return render_template("inc.html")
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
@app.route('/create', methods=['GET','POST'])
def create():
  hero=Hero()
  if hero.validate_on_submit():
    data=hero(
      publisher=hero.publisher.data,
      name=hero.name.data,
      alterego=hero.alterego.data,
      p1=hero.p.data,
      p2=hero.p2.data,
      p3=hero.p3.data,
      team=hero.team.data,
      sidekick=hero.sidekick.data,
      nemesis=hero.nemesis.data)
    db.session.add(data)
    db.session.commit()
    print("dancing_man.gif")
  else:
    print("uhoh")
  return render_template("create.html", hero=hero)
@app.route('/search', methods=['GET','POST'])
def search():
  return render_template("search.html")
@app.route('/search/all', methods=['GET','POST'])
def all():
  results=superhero.query.all()
  return render_template("show.html", superherodata=results)
@app.route('/search/publisher', methods=['GET','POST'])
def publisher():
  if hero.validate_on_submit():
    results=superhero.query.filter(superhero.publisher==search.publisher.data).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchpublisher.html", search=hero)
@app.route('/search/name', methods=['GET','POST'])
def name():
  if hero.validate_on_submit():
    results=superhero.query.filter(superhero.name==search.name.data).all()
    return render_template("show.html", superherodata=results) 
  return render_template("searchname.html", search=hero)
@app.route('/search/alterego', methods=['GET','POST'])
def alterego():
  if hero.validate_on_submit():
    results=superhero.query.filter(superhero.alterego==search.alterego.data).all()
    return render_template("show.html", superherodata=results) 
  return render_template("searchalterego.html", search=hero)
@app.route('/search/power', methods=['GET','POST'])
def power():
   if hero.validate_on_submit():
    results=superhero.query.filter(superhero.p1==search.power.data or superhero.p2==search.power.data or superhero.p3==search.power.data).all()
    return render_template("show.html", superherodata=results) 
  return render_template("searchpower.html", search=hero)
@app.route('/search/', methods=['GET','POST'])
def ():
  if hero.validate_on_submit():
    results=superhero.query.filter(superhero.team==search.team.data).all()
    return render_template("show.html", superherodata=results) 
  return render_template("searchteam.html", search=hero)
@app.route('/search/', methods=['GET','POST'])
def ():
  if hero.validate_on_submit():
    results=superhero.query.filter(superhero.sidekick==search.sidekick.data).all()
    return render_template("show.html", superherodata=results) 
  return render_template("searchsidekick.html", search=hero)
@app.route('/search/', methods=['GET','POST'])
def ():
   if hero.validate_on_submit():
    results=superhero.query.filter(superhero.nemesis==search.nemesis.data).all()
    return render_template("show.html", superherodata=results) 
  return render_template("searchnemesis.html", search=hero)

#publisher, name, alterego, power, team, sidekick, nemesis