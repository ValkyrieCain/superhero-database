from flask import render_template, redirect
from application import app
from application import db 
from application.models import School, Superheroes
from application.forms import FF, sch, hero, publisher, name, alterego, power,team, sidekick, nemesis
@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html")
@app.route('/abc')
def abc():
  return render_template("abc.html", body="hello my friends")
@app.route('/blog', methods=['GET','POST'])
def blog():
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
  hero=hero()
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
    print(GG.errors)
  return render_template("create.html", form=hero)
@app.route('/search', methods=['GET','POST'])
def search():
 searchfor=hero()
 publisher=publisher()
 name=name()
 alterego=alterego()
 power=power()
 team=team()
 sidekick=sidekick()
 nemesis=nemesis()

 if publisher.validate_on_submit():
  if hero.validate_on_submit():
    hero=superhero.query.filter(superhero.publisher==search.publisher.data).all()
    return render_template("show.html", superherodata=hero)
  return render_template("searchpublisher.html", form=search)

 if name.validate_on_submit():
  if hero.validate_on_submit():
    hero=superhero.query.filter(superhero.name==search.name.data).all()
    return render_template("show.html", superherodata=hero)
  return render_template("searchname.html", form=search)

 if alterego.validate_on_submit():
  if hero.validate_on_submit():
    hero=superhero.query.filter(superhero.alterego==search.alterego.data).all()
    return render_template("show.html", superherodata=hero)
  return render_template("searchalterego.html", form=search)

 if power.validate_on_submit():
  if hero.validate_on_submit():
    hero=superhero.query.filter(superhero.power==search.power.data).all()
    return render_template("show.html", superherodata=hero)
  return render_template("searchpower.html", form=search)

 if team.validate_on_submit():
  if hero.validate_on_submit():
    hero=superhero.query.filter(superhero.team==search.team.data).all()
    return render_template("show.html", superherodata=hero)
  return render_template("searchteam.html", form=search)

 if sidekick.validate_on_submit():
  if hero.validate_on_submit():
    hero=superhero.query.filter(superhero.sidekick==search.sidekick.data).all()
    return render_template("show.html", superherodata=hero)
  return render_template("searchsidekick.html", form=search)

 if nemesis.validate_on_submit():
  if hero.validate_on_submit():
    hero=superhero.query.filter(superhero.nemesis==search.nemesis.data).all()
    return render_template("show.html", superherodata=hero)
  return render_template("searchnemesis.html", form=search)

 return render_template("search.html", publisher=publisher,name=name,alterego=alterego,power=power,team=team,sidekick=sidekick,nemesis=nemesis)
 #publisher, name, alterego, power, team, sidekick, nemesis