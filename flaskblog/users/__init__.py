from flask import Blueprint

users_blueprint = Blueprint('users', __name__, url_prefix='/user')

from flaskblog.users import routes
