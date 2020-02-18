@app.route('/delete', methods=['GET','POST'])
def delete():
  delete=Delete()
  search=Search()
  if search.validate_on_submit():
    print("search function")
    x=Superheroes.query.filter(Superheroes.alterego==search.alterego.data.upper()).first()
    deletethis=x
    zz="zz"
    alt=search.alterego.data
    print(x)
    print(deletethis)
    print(zz)
    print(alt)
    if delete.validate_on_submit():
      print("delete function")
    else:
      print("second page loaded")
    return render_template('delete.html', data=deletethis, delete=delete)
  else:
    print("first page loaded")
  return render_template("searchalterego.html", search=search)