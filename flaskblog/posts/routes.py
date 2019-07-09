from flaskblog.posts import posts_blueprint


@posts_blueprint.route('/details')
def detailed_posts():
    return 'Detailed Posts'
