from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from application import routes
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DB_URI'))
app.config['SECRET_KEY'] = str(os.getenv('SK_NUM'))
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'