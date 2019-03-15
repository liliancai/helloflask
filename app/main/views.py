from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        input_name = form.name.data
        form.name.data = ''
        user = User.query.filter_by(username=input_name).first()
        if user is None:
            user = User(username=input_name)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            '''
            if app.config['FLASKY_ADMIN']:
                 send_email(app.config['FLASKY_ADMIN'],'New User',
						'mail/new_user',user=user)
            '''
        else:
            session['known'] = True
        session['name'] = input_name
        return redirect(url_for('.index'))
    return render_template('index.html',
        form=form, name=session.get('name'),
        known=session.get('known'))
