from . import main
from .. import db
from flask import render_template, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models import User
from .forms import EditProfileForm

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/usr/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@main.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        current_user.location = form.location.data
        current_user.about_me = form.about.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash("You've updated your profile")
        return redirect(url_for('.user', username=current_user.username))
    form.full_name.data = current_user.full_name
    form.location.data = current_user.location
    form.about.data = current_user.about_me
    return render_template('edit_profile.html', form=form)
