import datetime
from diary_app.users.constants import ADMIN_USERNAME
from diary_app.charts import chart_manager
from diary_app.events.constants import SEIZURE_EVENT_TYPE, AURA_EVENT_TYPE
from tests.utils import helpers


def test_get_chart():
    events_to_delete = []
    current_time = datetime.datetime.utcnow()

    event1 = helpers.create_test_event_by_date(
        current_time, SEIZURE_EVENT_TYPE)
    event2 = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=1), AURA_EVENT_TYPE)
    event3 = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=3), SEIZURE_EVENT_TYPE)
    event4 = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=5), AURA_EVENT_TYPE)
    event5 = helpers.create_test_event_by_date(
        current_time - datetime.timedelta(days=15), SEIZURE_EVENT_TYPE)
    events_to_delete.extend(
        [event1.id, event2.id, event3.id, event4.id, event5.id])

    try:
        chart_url = chart_manager.get_chart(ADMIN_USERNAME)
        print "CHART_URL: " + chart_url
        assert chart_url is not None
    finally:
        helpers.delete_events(events_to_delete)
