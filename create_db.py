from diary_app.database import db, init_db
from diary_app.events.models import Event, EventTrackingStatus
from diary_app.users.models import User
from diary_app.users.constants import ADMIN_USERNAME
from diary_app.events.constants import EVENT_TRACKING_STATUS_TYPES
import datetime

"""
DO NOT RUN THIS SCRIPT IN ''PROD'' IF DATABASE ALREADY HAS LIVE DATA!
"""

# # Drop and recreate DB
init_db()

print "DB tables created"

# # Insert Admin User
admin_user = User(ADMIN_USERNAME)
db.add(admin_user)
db.commit()

print "User table loaded"

# # Insert Event Tracking Status Type
for status in EVENT_TRACKING_STATUS_TYPES:
    event_tracking_status = EventTrackingStatus(status)
    db.add(event_tracking_status)
db.commit()

print "Event Tracking Status Types loaded"

# # Insert Test Event
# current_time = datetime.datetime.now()
# event_complete = Event(User.query.filter_by(
#     username=ADMIN_USERNAME).first().id,
#     current_time, 'AURA', 3, 2, 'COMPLETE')
# event_complete1 = Event(User.query.filter_by(
#     username=ADMIN_USERNAME).first().id,
#     current_time - datetime.timedelta(days=3), 'SEIZURE', 3, 2, 'COMPLETE')
# event_complete2 = Event(User.query.filter_by(
#     username=ADMIN_USERNAME).first().id,
#     current_time - datetime.timedelta(days=5), 'SEIZURE', 3, 2, 'COMPLETE')
# event_complete3 = Event(User.query.filter_by(
#     username=ADMIN_USERNAME).first().id,
#     current_time - datetime.timedelta(days=5), 'AURA', 3, 2, 'COMPLETE')
# event_complete4 = Event(User.query.filter_by(
#     username=ADMIN_USERNAME).first().id,
#     current_time - datetime.timedelta(days=15), 'SEIZURE', 3, 2, 'COMPLETE')
# event_incomplete = Event(User.query.filter_by(
#     username=ADMIN_USERNAME).first().id)
# db.add(event_complete)
# db.add(event_complete1)
# db.add(event_complete2)
# db.add(event_complete3)
# db.add(event_complete4)
# db.add(event_incomplete)
# db.commit()

print "Event table loaded"
