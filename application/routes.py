from flask import render_template, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Superheroes, Users
from application.forms import Hero, Search, Register, Login, Delete
import time
@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html")
#def forms():
#  GG=FF()
#  if GG.validate_on_submit():
#    HI=School(
#      id=GG.id.data,
#      name=GG.name.data)
#    db.session.add(HI)
#    db.session.commit()
#    print("dancing_man.gif")
#  else:
#    print("uhoh")
#    print(GG.errors)
#  return render_template("forms.html", form=GG)
@app.route('/register', methods=['GET','POST'])
def register():
  form=Register()
  if form.validate_on_submit():
    hash_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    data=Users(username=form.username.data, password=hash_pw)
    db.session.add(data)
    db.session.commit()
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)
@app.route('/login', methods=['GET','POST'])
def login():
  form=Login()
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  if form.validate_on_submit():
    user=Users.query.filter(Users.username==form.username.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      login_user(user)
      next_page = request.args.get('next')
      if next_page:
        return redirect(next_page)
      else:
        return redirect(url_for('home'))
  return render_template('login.html', title='Login', form=form)
@app.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('home'))
@app.route('/create', methods=['GET','POST'])
@login_required
def create():
  hero=Hero()
  if hero.validate_on_submit():
    data=Superheroes(
      publisher=hero.publisher.data.upper(),
      name=hero.name.data.upper(),
      alterego=hero.alterego.data.upper(),
      p1=hero.p1.data.upper(),
      p2=hero.p2.data.upper(),
      p3=hero.p3.data.upper(),
      team=hero.team.data.upper(),
      sidekick=hero.sidekick.data.upper(),
      nemesis=hero.nemesis.data.upper())
    db.session.add(data)
    db.session.commit()
    results=Superheroes.query.all()
    return redirect(url_for('saved'))
  return render_template("create.html", hero=hero)
@app.route('/update', methods=['GET','POST'])
@login_required
def update():
  update=Hero()
  search=Search()
  if search.validate_on_submit():
    result=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
    if update.validate_on_submit():
      result=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
      result.publisher=update.publisher.data.upper()
      result.name=update.name.data.upper()
      result.alterego=update.alterego.data.upper()
      result.p1=update.p1.data.upper()
      result.p2=update.p2.data.upper()
      result.p3=update.p3.data.upper()
      result.team=update.team.data.upper()
      result.sidekick=update.sidekick.data.upper()
      result.nemesis=update.nemesis.data.upper()
      db.session.commit()
      return redirect(url_for('saved'))
    return render_template('update.html', data=result, hero=update)
  return render_template("searchalterego.html", search=search)
@app.route('/delete', methods=['GET','POST'])
def delete():
  delete=Delete()
  search=Search()
  if search.validate_on_submit():
    if delete.validate_on_submit():
      result=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
      print(result)
      db.session.delete(result)
      db.session.commit()
      return redirect(url_for('saved'))
    else:
      print("uhoh")
      print(delete.errors)
    return render_template('delete.html', data=result, delete=delete)
  return render_template("searchalterego.html", search=search)
@app.route('/saved')
def saved():
  return render_template("saved.html")
  time.sleep(2)
  return redirect(url_for('home'))
@app.route('/search', methods=['GET','POST'])
def search():
  return render_template("search.html")
@app.route('/search/all', methods=['GET','POST'])
def all():
  results=Superheroes.query.all()
  return render_template("show.html", superherodata=results)
@app.route('/search/publisher', methods=['GET','POST'])
def publisher():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.publisher==search.publisher.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchpublisher.html", search=search)
@app.route('/search/name', methods=['GET','POST'])
def name():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.name==search.name.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchname.html", search=search)
@app.route('/search/alterego', methods=['GET','POST'])
def alterego():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchalterego.html", search=search)
@app.route('/search/power', methods=['GET','POST'])
def power():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.p1==search.power.data.upper() or Superheroes.p2==search.power.data.upper() or Superheroes.p3==search.power.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchpower.html", search=search)
@app.route('/search/team', methods=['GET','POST'])
def team():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.team==search.team.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchteam.html", search=search)
@app.route('/search/sidekick', methods=['GET','POST'])
def sidekick():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.sidekick==search.sidekick.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchsidekick.html", search=search)
@app.route('/search/nemesis', methods=['GET','POST'])
def nemesis():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.nemesis==search.nemesis.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchnemesis.html", search=search)

#publisher, name, alterego, power, team, sidekick, nemesis