from flask import render_template
from flaskblog.users import users_blueprint
from flaskblog.users.forms import RegistrationForm, LoginForm


@users_blueprint.route('/register')
def register_user():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@users_blueprint.route('/login')
def login_user():
    return 'login'
