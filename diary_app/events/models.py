from diary_app.utils import id_generator
from diary_app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    event_type = Column(String(128))
    event_severity = Column(Integer)
    event_duration = Column(Integer)
    event_time = Column(DateTime, default=func.now())
    record_created_at = Column(DateTime, default=func.now())
    last_updated = Column(DateTime, onupdate=func.now())
    user = relationship('User', backref=backref('jobs', lazy='dynamic'))

    def __init__(self, user_id, event_type=None, event_severity=None, event_duration=None):
        self.user_id = user_id
        self.event_type = event_type
        self.event_severity = event_severity
        self.event_duration = event_duration

    def __repr__(self):
        return '<Event  %r> for User: %s', [self.id, self.user.username]