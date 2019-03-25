import os
basedir = os.path.abspath(os.path.dirname(__file__))
# dbdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'databases')
dbdir = os.path.join(basedir, 'databases')
# print(dbdir)
#  print(basedir) # /helloflask


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'am a secret string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    # print(MAIL_SERVER)
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    # print(MAIL_PORT)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
    #    ['true', 'on', '1']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # print(MAIL_USERNAME)
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <2941758436@qq.com>'
    FLASKY_ADMIN = os.environ.get('FlASKY_ADMIN')
    # print(FLASKY_ADMIN)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 4

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(dbdir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
         'sqlite:///' + os.path.join(dbdir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
