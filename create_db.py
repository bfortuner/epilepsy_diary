from diary_app.database import db, init_db
from diary_app.events.models import Event
from diary_app.users.models import User
from diary_app.users.constants import ADMIN_USERNAME


"""
DO NOT RUN THIS SCRIPT IN ''PROD'' IF DATABASE ALREADY HAS LIVE DATA!
"""

# Drop and recreate DB
init_db()

print "DB tables created"

# # Insert Admin User
admin_user = User(ADMIN_USERNAME)
db.add(admin_user)
db.commit()

print "User table loaded"

# # Insert Test Event
event_complete = Event(User.query.filter_by(username=ADMIN_USERNAME).first().id, "seizure", 3, 2)
event_incomplete = Event(User.query.filter_by(username=ADMIN_USERNAME).first().id)
db.add(event_complete)
db.add(event_incomplete)
db.commit()

print "Event table loaded"