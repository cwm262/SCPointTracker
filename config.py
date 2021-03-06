import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_PER_PAGE = 10


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'oh my god Becky look at her butt'
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or 'super super super cereal secret'
    SECURITY_PASSWORD_SALT = 'my_precious_two'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgresql://pointsadmin:password123@localhost/scpt'
    # mail settings
    MAIL_DEFAULT_SENDER = "from@example.com"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}