from flask import Flask,url_for,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
from config import config
from .main import main as main_blueprint

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

def create_app(config_name):
	app=Flask(__name__)
	app.config.from_object(config[config_name])
	app.register_blueprint(main_blueprint)
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	db.init_app(app)
	
	return app


