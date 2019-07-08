from flask import Flask
import os
from flaskblog.users import users_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_BLOG_SECRET']
app.register_blueprint(users_blueprint)

from flaskblog import routes
