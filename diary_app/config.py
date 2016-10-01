import os
import logging


class Config(object):
    TESTING = False
    DEBUG = False
    WTF_CSRF_ENABLED = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = os.getenv('EPILEPSY_APP_SECRET_KEY', 'secret')
    DB_ISOLATION_LEVEL = 'READ UNCOMMITTED'
    PLOTLY_USERNAME = 'hapibot'
    PLOTLY_PASSWORD = os.getenv('EPILEPSY_PLOTLY_PASSWORD')


class ProdConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'EPILEPSY_DATABASE_URI')
    S3_USER_CHARTS_BUCKET = 'epilepsy-user-charts'
    APP_LOG_LEVEL = logging.INFO
    MAIL_LOG_LEVEL = logging.ERROR
    LOCAL_CHARTS_DIR_PATH = "/tmp/"
    CLIENT_AUTH_KEY = os.getenv('EPILEPSY_CLIENT_AUTH_KEY')


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'EPILEPSY_DATABASE_URI')
    # 'sqlite:///database.db' SQLite doesn't play well w SQLAlchemy :(
    S3_USER_CHARTS_BUCKET = 'test-epilepsy-user-charts'
    APP_LOG_LEVEL = logging.DEBUG
    MAIL_LOG_LEVEL = logging.ERROR
    LOCAL_CHARTS_DIR_PATH = "charts/"
    CLIENT_AUTH_KEY = 'testing'


config = globals()[os.getenv('EPILEPSY_CONFIG', 'TestConfig')]
