from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
db = SQLAlchemy()
from .main import main as main_blueprint
# from .auth import auth as auth_blueprint

bootstrap = Bootstrap()
mail = Mail()
print("Why you guess can't import me???")
login_manager = LoginManager()

def create_app(config_name):
	app=Flask(__name__)
	app.config.from_object(config[config_name])

	app.register_blueprint(main_blueprint)
	# app.register_blueprint(auth_blueprint, url_prefix='/auth')
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	db.init_app(app)
	#login_manager.init_app(app)

	return app
