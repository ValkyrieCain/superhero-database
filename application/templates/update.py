@app.route('/update', methods=['GET','POST'])
@login_required
def update():
  update=Hero()
  search=Search()
  if search.validate_on_submit():
    result=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
    print(result)
    print(search.alterego.data)
    print("search2")
    if update.validate_on_submit():
      print(result)
      print(search.alterego.data)
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
    else:
      print("uhoh")
    return render_template('update.html', data=result, hero=update)
  return render_template("searchalterego.html", search=search)