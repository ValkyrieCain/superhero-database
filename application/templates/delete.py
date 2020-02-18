@app.route('/delete', methods=['GET','POST'])
@login_required
def delete():
  delete=Delete()
  search=Search()
  if search.validate_on_submit():
    deletethis=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
    print(deletethis)
    print(search.alterego.data)
    print("search1")
    if delete.validate_on_submit():
      print("delete1")
      print(deletethis)
      print(search.alterego.data)
      db.session.delete(deletethis)
      db.session.commit()
      return redirect(url_for('saved'))
    else:
      print("bad",delete.errors)
    return render_template('delete.html', data=deletethis, delete=delete)
  else:print("even worse",search.errors)
  return render_template("searchalterego.html", search=search)