#from diary_app.users.constants import *
from diary_app.utils import id_generator
from diary_app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(128))
    created_at = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, onupdate=func.now())
    event = relationship('Event', backref=backref('users'))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % (self.username)