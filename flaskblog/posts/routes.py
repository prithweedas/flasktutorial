from flask import Blueprint

posts_blueprint = Blueprint('posts', __name__, url_prefix='/post')

from flaskblog.posts.models import Post


@posts_blueprint.route('/details')
def detailed_posts():
    return 'Detailed Posts'
