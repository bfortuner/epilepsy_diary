from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.functions import database_exists, create_database
from diary_app.config import config

#http://sqlalchemy-utils.readthedocs.org/en/latest/database_helpers.html
engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
						convert_unicode=True,
						isolation_level=config.DB_ISOLATION_LEVEL,
						pool_recycle=3600)

if 'sqlite' in config.SQLALCHEMY_DATABASE_URI and not database_exists(engine.url):
	create_database(engine.url)

db = scoped_session(sessionmaker(autocommit=False,
								 autoflush=False,
								 bind=engine))
Base = declarative_base()
Base.query = db.query_property()

from diary_app.users.models import User
from diary_app.events.models import Event

def init_db():
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)