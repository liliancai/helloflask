from flask import make_response
from flask import request
from flask import redirect
import os
from flask_migrate import Migrate
def page_not_found(e):
    return render_template('500.html'), 500

session = {}
@app.route('/',methods=['GET', 'POST'])
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(to, subject, template, **kwargs):
	msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
					sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	thr = Thread(target=send_async_email, args=[app, msg])
	thr.start()
	return thr

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
