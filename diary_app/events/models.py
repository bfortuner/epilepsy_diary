#from diary_app.users.constants import *
from diary_app.utils import id_generator
from diary_app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    username = Column(String(128))
    created_at = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, onupdate=func.now())
    user = relationship('User', backref=backref('events'))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return '<User %r>' % (self.username)