from flask import Flask, render_template
from flask import make_response
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
'''
from flask import redirect
from flask import request
'''
app=Flask(__name__)
app.config['SECRET_KEY'] = 'am a secret string'
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/',methods=['GET', 'POST'])
@app.route('/usr/<name>')
def usr(name=''):
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


class NameForm(FlaskForm):
    """
        StringField handles <input type= "text">
        SubmitFiled handles        type = "submit"
    """
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('submit')

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
