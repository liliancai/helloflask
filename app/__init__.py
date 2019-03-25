from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager
from flask_pagedown import PageDown

# print(Mail.__name__)
# print(__name__) #app
# print(config.__name__) # dict object has not atribute __name__
db = SQLAlchemy()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
pagedown = PageDown()
# print("Why you guess can't import me???")
# cause import .main above db, and .main has # BUG:

login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    return app
