from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
app.config['SECRET_KEY'] = str(os.getenv('SK_NUM'))
db = SQLAlchemy(app)
login = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)
from application import routes