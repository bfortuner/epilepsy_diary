from diary_app import db
from diary_app.events.models import Event


def get_event(event_id):
    event = Event.query.filter_by(id=event_id).first()
    return event


def get_user_events(user_id):
    pass


def create_event(user_id, event_time, event_type, severity, duration):
    event = Event(user_id, event_time, event_type, severity, duration)
    db.add(event)
    db.commit()
    return event


def delete_event(event_id):
    Event.query.filter_by(id=event_id).delete()
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
    attribs_required_for_complete_event = 3
    event = get_event(event_id)
    if event.event_type is not None:
        attribs_required_for_complete_event -= 1
    if event.event_severity is not None:
        attribs_required_for_complete_event -= 1
    if event.event_duration is not None:
        attribs_required_for_complete_event -= 1

    if attribs_required_for_complete_event == 0:
        event.event_tracking_status_name = 'COMPLETE'
    elif attribs_required_for_complete_event < 3:
        event.event_tracking_status_name = 'PARTIALLY_COMPLETE'
    db.commit()
