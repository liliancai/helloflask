from flask import render_template, flash, url_for, redirect, request
from . import auth
from flask_login import login_user,logout_user
from .forms import LoginForm
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remeber_me.data)
            next = request.args.get("next")
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        # else
        flash('Invalid username or password :(')
    return render_template('auth/login.html', form=form)

@auth.route('/logout', methods=['GET','POST'])
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
