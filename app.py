from flask import Flask, render_template
from flask import make_response
from flask_bootstrap import Bootstrap
'''
from flask import redirect
from flask import request
'''
app=Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def hello():
   # user_agent = request.headers.get('User-Agent')
   # return '<h1>Your browser is {}</h1>'.format(user_agent)
#   return 'Bad Request', 400
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response
'''
@app.route('/')
def index():
	return redirect('https://google.se')

@app.route('/usr/<name>')
def usr(name):
	return '<h1>Hello, {}!</h1>'.format(name)
'''

@app.route('/usr/<name>')
def usr(name):
	return render_template('user.html', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
