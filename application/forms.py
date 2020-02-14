from flask_wtf import FlaskForm
from wtforms import (BooleanField,DateField,DateTimeField,DecimalField,
FileField,MultipleFileField,FloatField,IntegerField,SelectField,
SelectMultipleField,SubmitField,StringField,HiddenField,PasswordField,
TextAreaField)
from wtforms.validators import DataRequired, Length

class FF(FlaskForm):
  boolean=BooleanField()
  date=DateField()
  datetime=DateTimeField()
  decimal=DecimalField()
  file=FileField()
  multiplefile=MultipleFileField()
  float=FloatField()
  integer=IntegerField()
  select=SelectField()
  selectmultiple=SelectMultipleField()
  string=StringField()
  hidden=HiddenField()
  password=PasswordField()
  textarea=TextAreaField()
  boolean2=BooleanField()
  id=IntegerField()
  name=StringField()
  submit=SubmitField()
