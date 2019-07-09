from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flaskblog.users import users_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_BLOG_SECRET']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['FLASK_BLOG_DB_URL']
app.register_blueprint(users_blueprint)
db = SQLAlchemy(app)

from flaskblog import routes
from flaskblog.users import models
