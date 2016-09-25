import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS
from diary_app.config import config
# from diary_app.database import db
# from diary_app.utils.constants import *


# Initialize App
application = Flask(__name__)
CORS(application)
application.config.from_object('diary_app.config.TestConfig')  #+ os.getenv('TestConfig'))

# Initialize Logging
'''
from diary_app.utils import logger
application.logger.addHandler(logger.get_rotating_file_handler(APP_LOG_FILE))
items_log = logger.get_logger(JOB_ITEMS_LOG_FILE, log_level=LOG_LEVEL)
tasks_log = logger.get_logger(TASKS_LOG_FILE,  log_level=LOG_LEVEL)
jobs_log = logger.get_logger(JOBS_LOG_FILE, log_level=LOG_LEVEL)
'''

# Import APIs
import diary_app.users.api
import diary_app.events.api

# @application.teardown_appcontext
# def shutdown_session(exception=None):
# 	db.remove()