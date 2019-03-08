from flask import Flask,url_for,render_template
from flask import make_response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import request
from flask import redirect
import os
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SECRET_KEY'] = 'am a secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

session = {}
@app.route('/',methods=['GET', 'POST'])
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
        else:
            session['known'] = True
        session['name'] = input_name
        return redirect(url_for('index'))
    return render_template('index.html',
        form=form, name=session.get('name'),
        known=session.get('known'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


class NameForm(FlaskForm):
    """
        StringField handles <input type= "text">
        SubmitFiled handles        type = "submit"
    """
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('submit')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
    	return '<Role %r>' % self.name
    # backref attribute can be used for users access role instead using role_id
    # Role User one-to-many 12s, uselist =False -> 121
    users = db.relationship('User', backref='role')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)

    def __repr__(self):
	       return '<User %r>' % self.username
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

'''
@app.route('/')
def hello():
    # user_agent = request.headers.get('User-Agent')
    # return '<h1>Your browser is {}</h1>'.format(user_agent)
    #   return 'Bad Request', 400
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
'''
'''
@app.route('/')
def index():
    return redirect('https://google.se')

@app.route('/usr/<name>')
def usr(name):
    return '<h1>Hello, {}!</h1>'.format(name)
'''
