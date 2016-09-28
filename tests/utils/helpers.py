from diary_app import db
from diary_app.events import event_manager
from diary_app.events.models import Event
from diary_app.users.models import User
from diary_app.users.constants import ADMIN_USERNAME


def cleanup(event_id):
    event_manager.delete_event(event_id)


def delete_events(event_ids):
    for event_id in event_ids:
        event_manager.delete_event(event_id)


def create_test_event_w_status(tracking_status):
    event = Event(User.query.filter_by(username=ADMIN_USERNAME).first().id,
                  event_tracking_status=tracking_status)
    db.add(event)
    db.commit()
    return event


def create_test_event():
    event = Event(User.query.filter_by(username=ADMIN_USERNAME).first().id)
    db.add(event)
    db.commit()
    return event


def create_test_event_by_date(event_time, event_type):
    event = Event(User.query.filter_by(
        username=ADMIN_USERNAME).first().id,
        event_time=event_time,
        event_type=event_type)
    db.add(event)
    db.commit()
    return event
