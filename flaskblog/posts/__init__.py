from flask import Blueprint

posts_blueprint = Blueprint('posts', __name__, url_prefix='/post')

from flaskblog.posts import routes
