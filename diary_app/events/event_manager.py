from diary_app import db
from sqlalchemy.sql import func
from diary_app.events.models import Event
from diary_app.users import user_manager


def get_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    return event


def get_events_in_date_range(username, start_time, end_time, event_type):
    user = user_manager.get_or_create_user(username)
    events = (db.query(Event)
        .filter(Event.event_time.between(start_time, end_time))
        .filter_by(user_id=user.id)
        .filter_by(event_type=event_type)
        .all())
    return events


def get_event_count_in_date_range(username, start_time, end_time, event_type):
    """
    Returns list of tuples (date, count) ordered by date ASC
    e.g. [(u'2016-09-24', 1), (u'2016-09-27', 2)]
    """
    user = user_manager.get_or_create_user(username)
    count_by_day = (db.query(func.DATE(Event.event_time), func.count(Event.id))
        .filter(Event.event_time.between(start_time, end_time))
        .filter_by(user_id=user.id)
        .filter_by(event_type=event_type)
<<<<<<< HEAD
        .filter_by(event_tracking_status_name="COMPLETE")
=======
>>>>>>> dev
        .group_by(func.DATE(Event.event_time))
        .order_by(func.DATE(Event.event_time).asc())
        .all())
    return count_by_day


<<<<<<< HEAD
def create_event(user_id, event_time,
        event_type=None, severity=None, duration=None):
=======
def create_event(user_id, event_time, event_type, severity, duration):
>>>>>>> dev
    event = Event(user_id, event_time, event_type, severity, duration)
    db.add(event)
    db.commit()
    return event


def delete_event(event_id):
    Event.query.filter_by(id=event_id).delete()
    db.commit()


def update_event(event):
    db.commit()


def update_event_type(event_id, event_type):
    event = get_event(event_id)
    event.event_type = event_type
    db.commit()


def update_event_duration(event_id, duration):
    event = get_event(event_id)
    event.event_duration = duration
    db.commit()


def update_event_severity(event_id, severity):
    event = get_event(event_id)
    event.event_severity = severity
    db.commit()


def update_event_tracking_status(event_id):
    attribs_required_for_complete_event = 2
    event = get_event(event_id)
    if event.event_type is not None:
        attribs_required_for_complete_event -= 1
    # if event.event_severity is not None:
    #     attribs_required_for_complete_event -= 1
    if event.event_duration is not None:
        attribs_required_for_complete_event -= 1

    if attribs_required_for_complete_event == 0:
        event.event_tracking_status_name = 'COMPLETE'
    elif attribs_required_for_complete_event < 2:
        event.event_tracking_status_name = 'PARTIALLY_COMPLETE'
    else:
        event.event_tracking_status_name = 'CREATED'
    db.commit()
