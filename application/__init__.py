from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
app.config['SECRET_KEY'] = str(os.getenv('SK_NUM'))
db = SQLAlchemy(app)

from application import routes
