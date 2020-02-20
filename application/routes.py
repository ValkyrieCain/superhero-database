from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, current_user, logout_user, login_required
from application import app, db, bcrypt, login_manager
from application.models import Superheroes, Users, Powers
import pandas
from application.forms import Hero, Search, Register, Login, Delete, Alterego
import time
#def show(x):
#  final={}
#  final[Publisher]=x[Publisher]
#  final["Name"]=x[Name]
#  final["Alterego"]=x["Alterego"]
#  p1id=Powers.query.filter(Powers.power==x["p1"].upper()).first()
#  p2id=Powers.query.filter(Powers.power==x["p2"].upper()).first()
#  p3id=Powers.query.filter(Powers.power==x["p3"].upper()).first()
#  final["First Power"]=p1.id
#  final["Second Power"]=p2.id
#  final["Third Power"]=p3.id
#  final["Team"]=x["Team"]
#  final["Sidekick"]=x["Sidekick"]
#  final["Nemesis"]=x["Nemesis"]
#  return final
@app.route('/')
@app.route('/home')
def home():
  return render_template("home.html")
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
    p1=Powers(power=hero.p1.data.upper())
    p2=Powers(power=hero.p2.data.upper())
    p3=Powers(power=hero.p3.data.upper())
    db.session.bulk_save_objects([p1,p2,p3])
    db.session.commit()
    p1id=Powers.query.filter(Powers.power==hero.p1.data.upper()).first()
    p2id=Powers.query.filter(Powers.power==hero.p2.data.upper()).first()
    p3id=Powers.query.filter(Powers.power==hero.p3.data.upper()).first()
    data=Superheroes(
      publisher=hero.publisher.data.upper(),
      name=hero.name.data.upper(),
      alterego=hero.alterego.data.upper(),
      #p1=hero.p1.data.upper(),
      #p2=hero.p2.data.upper(),
      #p3=hero.p3.data.upper(),
      p1=p1id.id,
      p2=p2id.id,
      p3=p3id.id,
      team=hero.team.data.upper(),
      sidekick=hero.sidekick.data.upper(),
      nemesis=hero.nemesis.data.upper())
    db.session.add(data)
    db.session.commit()
    return redirect(url_for('saved'))
  return render_template("create.html", hero=hero)
@app.route('/update', methods=['GET','POST'])
@login_required
def update():
  update=Hero()
  search=Alterego()
  if search.validate_on_submit():
    result=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
    if update.validate_on_submit():
      result.publisher=update.publisher.data.upper()
      result.name=update.name.data.upper()
      result.alterego=search.alterego.data.upper()
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
@login_required
def delete():
  search=Alterego()
  if search.validate_on_submit():
    ae=search.alterego.data
    return redirect("/delete/"+ae)
  return render_template("searchalterego.html", search=search)
@app.route('/delete/<ae>', methods=['GET','POST'])
def deleteconfirm(ae):
  delete=Delete()
  deletethis=Superheroes.query.filter(Superheroes.alterego==ae.upper()).first()
  if delete.validate_on_submit():
    db.session.delete(deletethis)
    db.session.commit()
    return redirect(url_for('saved'))
  return render_template('delete.html', data=deletethis, delete=delete)
@app.route('/saved')
def saved():
  return render_template("saved.html")
  time.sleep(1)
  return redirect(url_for('home'))
@app.route('/search', methods=['GET','POST'])
def search():
  return render_template("search.html")
#@app.route('/search/results/', methods=['GET','POST'])
  #data=Search()
  #for x in pub:
  #  search.x=pub.x
  #return render_template("saved.html")#, superherodata=data)
@app.route('/search/all', methods=['GET','POST'])
def all():
  results=Superheroes.query.all()
  return render_template("show.html", superherodata=results)
@app.route('/search/publisher', methods=['GET','POST'])
def publisher():
  search=Search()
  if search.validate_on_submit():
    results=Superheroes.query.filter(Superheroes.publisher==search.publisher.data.upper()).all()
    #print(results.publisher.data)
    p1=0
    p2=0
    p3=0
    print(111111111111111)
    for x in results:
      p1=int(x.__dict__['p1'])
      p2=int(x.__dict__['p2'])
      p3=int(x.__dict__['p3'])
    print(p1+4)
    print(p2)
    print(111111111111111)
    p1id=Powers.query.filter(Powers.id==p1).first()
    p2id=Powers.query.filter(Powers.id==p2).first()
    p3id=Powers.query.filter(Powers.id==p3).first()
    print(111111111111111)
    print(p1id)
    print(p2)
    print(p3id)
    #powers=Powers.query.filter(Powers.id==8).first()
    print(222)
    #print(powers)
    print(111111111111111)
    #return redirect(url_for('saved'))
    #print(powers)#{"p1":"","p2":"","p3":""}]
    #for x in results:
    #  powers.p1=Powers.query.filter(Powers.id==x.p1)
    #  powers.p2=Powers.query.filter(Powers.id==x.p2)
    #  powers.p3=Powers.query.filter(Powers.id==x.p3)
    return render_template("show.html", superherodata=results, p1id=p1id, p2id=p2id, p3id=p3id)#, powerdata=powers)
    #{%for x in powerdata%}
    #  <tr>
    #   <td>{{x.power}}</td>
    #  </tr>
    # {%endfor%}
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
    results=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
    p1=0
    p2=0
    p3=0
    for x in results:
      p1=int(x.__dict__['p1'])
      p2=int(x.__dict__['p2'])
      p3=int(x.__dict__['p3'])
    p1id=Powers.query.filter(Powers.id==p1).first()
    p2id=Powers.query.filter(Powers.id==p2).first()
    p3id=Powers.query.filter(Powers.id==p3).first()
    return render_template("show.html", superherodata=results, p1id=p1id, p2id=p2id, p3id=p3id)
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