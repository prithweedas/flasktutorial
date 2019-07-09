from flask import render_template, flash, redirect, url_for, Blueprint
from flaskblog.users.forms import RegistrationForm, LoginForm

users_blueprint = Blueprint('users', __name__, url_prefix='/user')
from flaskblog.users.models import User
from flaskblog import db, bcrypt


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data,
                        password=hashed_password, email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.login_user'))
    return render_template('register.html', title='Register', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Success fully loggedin', 'success')
        return redirect(url_for('index'))

    return render_template('login.html', title='Login', form=form)
