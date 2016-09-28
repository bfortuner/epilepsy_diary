import os
import logging


class Config(object):
    TESTING = False
    DEBUG = False
    WTF_CSRF_ENABLED = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    PLOTLY_USERNAME = "hapibot"
    PLOTLY_PASSWORD = "ix1yikrn67"
    SECRET_KEY = os.getenv('APP_SECRET_KEY', 'secret')
    LOCAL_CHARTS_DIR_PATH = "charts/"
    DB_ISOLATION_LEVEL = 'READ UNCOMMITTED'
    PLOTLY_PASSWORD = 'ix1yikrn67'
    PLOTLY_USERNAME = 'hapibot'
    # AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID', 'password')
    # AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'password')


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'EPILEPSY_DATABASE_URI', 'sqlite:///database.db')
    S3_USER_CHARTS_BUCKET = 'epilepsy-user-charts'
    APP_LOG_LEVEL = logging.INFO
    MAIL_LOG_LEVEL = logging.ERROR


class TestConfig(Config):
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    S3_USER_CHARTS_BUCKET = 'test-epilepsy-user-charts'
    APP_LOG_LEVEL = logging.DEBUG
    MAIL_LOG_LEVEL = logging.ERROR


config = globals()[os.getenv('EPILEPSY_CONFIG', 'TestConfig')]
