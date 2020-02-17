from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
app.config['SECRET_KEY'] = str(os.getenv('SK_NUM'))
db = SQLAlchemy(app)
from application import routes