from diary_app import db
from diary_app.users.models import User

def get_or_create_user(username):
	user = User.query.filter_by(username=username).first()
	if user is None:
		user = User(username)
		db.add(user)
		db.commit()
	return user

def get_events_by_user(username):
	user = User.query.filter_by(username).first()
	events = user.events.all()
	return events

def get_user_by_id(user_id):
	return User.query.get(user_id)