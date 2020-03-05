from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Superheroes, Users, Powers
from application.forms import Hero, Search, Register, Login, Delete, Alterego, Alteregocreate, Dontdelete, Multidelete
import time
@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html")
@app.route('/delete', methods=['GET','POST'])
def delete():
  delete=Delete()
  dontdelete=Dontdelete()
  multidelete=Multidelete()
  if multidelete.dontdelete.validate_on_submit():
    print("no")
    return redirect("/home")
  if multidelete.delete.validate_on_submit():
    print("yes")
    return redirect(url_for('saved'))
  if dontdelete.submit.validate_on_submit():
    print("no")
    return redirect("/home")
  if delete.submit.validate_on_submit():
    print("yes")
    return redirect(url_for('saved'))
  return render_template('delete.html', multidelete=multidelete, delete=delete, dontdelete=dontdelete)




@app.route('/saved')
def saved():
  return render_template("saved.html")
  time.sleep(1)
  return redirect(url_for('home'))
@app.route('/search', methods=['GET','POST'])
def search():
  return render_template("search.html")
@app.route('/search/all', methods=['GET','POST'])
def all():
  results=Superheroes.query.all()
  p1=0
  p2=0
  p3=0
  p1id=""
  p2id=""
  p3id=""
  for x in results:
    p1=int(x.__dict__['p1'])
    p1id=Powers.query.filter(Powers.id==p1).first()
    x.__dict__['p1']=p1id.power
    p2=int(x.__dict__['p2'])
    p2id=Powers.query.filter(Powers.id==p2).first()
    x.__dict__['p2']=p2id.power
    p3=int(x.__dict__['p3'])
    p3id=Powers.query.filter(Powers.id==p3).first()
    x.__dict__['p3']=p3id.power
  return render_template("show.html", superherodata=results)
@app.route('/search/publisher', methods=['GET','POST'])
def publisher():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.publisher==search.publisher.data.upper()).all()
    p1=0
    p2=0
    p3=0
    p1id=""
    p2id=""
    p3id=""
    for x in results:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    return render_template("show.html", superherodata=results)
  return render_template("searchpublisher.html", search=search)
@app.route('/search/name', methods=['GET','POST'])
def name():
  search=Search()
  if search.validate_on_submit():
    print(search.name.data)
    results=Superheroes.query.filter(Superheroes.name==search.name.data.upper()).all()
    return render_template("show.html", superherodata=results)
  return render_template("searchname.html", search=search)
@app.route('/search/alterego', methods=['GET','POST'])
def alterego():
  search=Alterego()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).all()
    p1=0
    p2=0
    p3=0
    p1id=""
    p2id=""
    p3id=""
    for x in results:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    return render_template("show.html", superherodata=results)
  return render_template("searchalterego.html", search=search)
@app.route('/search/power', methods=['GET','POST'])
def power():
  search=Search()
  if search.validate_on_submit():
    #pquery=Powers.query.filter(Powers.power.in_(search.power.data.upper())).first()
    pquery=Powers.query.filter(Powers.power==search.power.data.upper()).first()
    p1q=Superheroes.query.filter(Superheroes.p1==pquery.id).all()
    p2q=Superheroes.query.filter(Superheroes.p2==pquery.id).all()
    p3q=Superheroes.query.filter(Superheroes.p3==pquery.id).all()
    #results=Superheroes.query.filter(Superheroes.p1==pquery.id, Superheroes.p2==pquery.id, Superheroes.p3==pquery.id).all()
    p1=0
    p2=0
    p3=0
    p1id=""
    p2id=""
    p3id=""
    for x in p1q:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    for x in p2q:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    for x in p3q:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    return render_template("showpowers.html", p1=p1q, p2=p2q, p3=p3q)
  return render_template("searchpower.html", search=search)
@app.route('/search/team', methods=['GET','POST'])
def team():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.team==search.team.data.upper()).all()
    p1=0
    p2=0
    p3=0
    p1id=""
    p2id=""
    p3id=""
    for x in results:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    return render_template("show.html", superherodata=results)
  return render_template("searchteam.html", search=search)
@app.route('/search/sidekick', methods=['GET','POST'])
def sidekick():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.sidekick==search.sidekick.data.upper()).all()
    p1=0
    p2=0
    p3=0
    p1id=""
    p2id=""
    p3id=""
    for x in results:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    return render_template("show.html", superherodata=results)
  return render_template("searchsidekick.html", search=search)
@app.route('/search/nemesis', methods=['GET','POST'])
def nemesis():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.nemesis==search.nemesis.data.upper()).all()
    p1=0
    p2=0
    p3=0
    p1id=""
    p2id=""
    p3id=""
    for x in results:
      p1=int(x.__dict__['p1'])
      p1id=Powers.query.filter(Powers.id==p1).first()
      x.__dict__['p1']=p1id.power
      p2=int(x.__dict__['p2'])
      p2id=Powers.query.filter(Powers.id==p2).first()
      x.__dict__['p2']=p2id.power
      p3=int(x.__dict__['p3'])
      p3id=Powers.query.filter(Powers.id==p3).first()
      x.__dict__['p3']=p3id.power
    return render_template("show.html", superherodata=results)
  return render_template("searchnemesis.html", search=search)

#publisher, name, alterego, power, team, sidekick, nemesis