from flask import render_template, flash, redirect, url_for, Blueprint
from flaskblog.users.forms import RegistrationForm, LoginForm
from flask_login import login_user as user_login, current_user, logout_user as user_logout, login_required

users_blueprint = Blueprint('users', __name__, url_prefix='/user')
from flaskblog.users.models import User
from flaskblog import db, bcrypt


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            user_login(user, remember=form.remember.data)
            return redirect(url_for('index'))
        else:
            flash(f'Login Unsuccessful', 'danger')

    return render_template('login.html', title='Login', form=form)


@users_blueprint.route('/logout')
def logout_user():
    user_logout()
    return redirect(url_for('index'))


@users_blueprint.route('/account')
def user_account():
    return render_template('account.html', title='Account')
