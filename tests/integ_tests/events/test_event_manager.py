import datetime
from diary_app.events import event_manager
from diary_app.events.constants import SEIZURE_EVENT_TYPE, AURA_EVENT_TYPE
from diary_app.users import user_manager
from diary_app.users.constants import ADMIN_USERNAME
from tests.utils import helpers


def test_create_event():
    event = helpers.create_test_event()
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event is not None
    assert fetched_event.id == event.id

    helpers.cleanup(event.id)


def test_get_events_in_date_range():
    events_to_delete = []
    current_time = datetime.datetime.utcnow()
    start_time = current_time - datetime.timedelta(days=2)
    end_time = current_time

    event_before_start = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=5), SEIZURE_EVENT_TYPE)
    event_inside_date_range = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=1), SEIZURE_EVENT_TYPE)
    event_after_start = helpers.create_test_event_by_date(
        current_time + datetime.timedelta(days=1), SEIZURE_EVENT_TYPE)
    events_to_delete.extend(
        [event_before_start.id, event_inside_date_range.id,
            event_after_start.id])

    try:
        user_events = user_manager.get_events(ADMIN_USERNAME)
        assert len(user_events) == 3

        user_events_in_date_range = event_manager.get_events_in_date_range(
            username=ADMIN_USERNAME,
            start_time=start_time,
            end_time=end_time,
            event_type=SEIZURE_EVENT_TYPE)
        assert len(user_events_in_date_range) == 1
        assert user_events_in_date_range[0].id == event_inside_date_range.id
    finally:
        helpers.delete_events(events_to_delete)


def test_get_event_count_in_date_range():
    events_to_delete = []
    current_time = datetime.datetime(2016, 1, 1, 20, 0, 0)
    start_time = current_time - datetime.timedelta(days=5)
    end_time = current_time

    event_before_start = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=10), SEIZURE_EVENT_TYPE)

    event_inside_date_range = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(hours=1), SEIZURE_EVENT_TYPE)
    event_inside_date_range2 = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(hours=10), AURA_EVENT_TYPE)
    event_inside_date_range3 = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=3), AURA_EVENT_TYPE)

    event_after_start = helpers.create_test_event_by_date(
        current_time + datetime.timedelta(days=1), AURA_EVENT_TYPE)
    events_to_delete.extend(
        [event_before_start.id, event_inside_date_range.id,
            event_after_start.id, event_inside_date_range2.id,
            event_inside_date_range3.id])

    try:
        user_events_count = event_manager.get_event_count_in_date_range(
            username=ADMIN_USERNAME,
            start_time=start_time,
            end_time=end_time)

        # Seizures
        assert user_events_count[0][1] == 0
        assert user_events_count[1][1] == 1

        # Auras
        assert user_events_count[0][2] == 1
        assert user_events_count[1][2] == 1

    finally:
        helpers.delete_events(events_to_delete)


def test_delete_event():
    event = helpers.create_test_event()
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event is not None
    event_manager.delete_event(event.id)
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event is None

    helpers.cleanup(event.id)


def test_update_event_type():
    event = helpers.create_test_event()
    assert event.event_type is None
    event_manager.update_event_type(event.id, AURA_EVENT_TYPE)
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event.event_type == AURA_EVENT_TYPE

    helpers.cleanup(event.id)


def test_update_event_duration():
    event = helpers.create_test_event()
    assert event.event_duration is None
    event_manager.update_event_duration(event.id, "1-3")
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event.event_duration == "1-3"

    helpers.cleanup(event.id)


def test_update_event_severity():
    event = helpers.create_test_event()
    assert event.event_severity is None
    event_manager.update_event_severity(event.id, 5)
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event.event_severity == 5

    helpers.cleanup(event.id)


def test_update_event_tracking_status():
    event = helpers.create_test_event()
    assert event.event_tracking_status_name == 'CREATED'

    event_manager.update_event_type(event.id, AURA_EVENT_TYPE)
    event_manager.update_event_tracking_status(event.id)
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event.event_tracking_status_name == 'PARTIALLY_COMPLETE'

    event_manager.update_event_severity(event.id, 4)
    event_manager.update_event_tracking_status(event.id)
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event.event_tracking_status_name == 'PARTIALLY_COMPLETE'

    event_manager.update_event_duration(event.id, 80)
    event_manager.update_event_tracking_status(event.id)
    fetched_event = event_manager.get_event(event.id)
    assert fetched_event.event_tracking_status_name == 'COMPLETE'

    helpers.cleanup(event.id)
