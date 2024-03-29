from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_BLOG_SECRET']
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login_user'
login_manager.login_message_category = 'info'

from flaskblog.users.routes import users_blueprint
from flaskblog.posts.routes import posts_blueprint

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['FLASK_BLOG_DB_URL']
app.register_blueprint(users_blueprint)
app.register_blueprint(posts_blueprint)

from flaskblog import routes
from flaskblog.users import models
from flaskblog.posts import models
