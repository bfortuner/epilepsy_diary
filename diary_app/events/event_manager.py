from diary_app import db
from sqlalchemy.sql import case, func
from diary_app.events.models import Event
from diary_app.users import user_manager
from diary_app.events.constants import SEIZURE_EVENT_TYPE, AURA_EVENT_TYPE


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


def get_event_count_in_date_range(username, start_time, end_time):
    """
    Returns list of tuples (date, count1, count2) ordered by date ASC
    e.g. [(datetime(), 1, 2), (datetime(), 2, 0)]
    """
    user = user_manager.get_or_create_user(username)
    seizure_count_case_when = (case(
        [(Event.event_type == SEIZURE_EVENT_TYPE, 1), ], else_=0)
        .label(SEIZURE_EVENT_TYPE))

    aura_count_case_when = (case(
        [(Event.event_type == AURA_EVENT_TYPE, 1), ],
        else_=0).label(AURA_EVENT_TYPE))

    result = (db.query(func.date(Event.event_time),
                       func.sum(seizure_count_case_when),
                       func.sum(aura_count_case_when))
              .filter_by(user_id=user.id)
              .filter_by(event_tracking_status_name="COMPLETE")
              .filter(Event.event_time.between(start_time, end_time))
              .group_by(func.date(Event.event_time))
              .order_by(func.date(Event.event_time).asc())
              .all())
    print "Returning query result " + str(result)
    return result


def create_event(user_id, event_time,
                 event_type=None, severity=None, duration=None):
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
