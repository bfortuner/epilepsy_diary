from diary_app import db
from diary_app.users.models import User
from diary_app.events.models import Event
from diary_app.events import event_manager
from diary_app.users.constants import ADMIN_USERNAME

def test_create_event():
	event = create_test_event()
	fetched_event = event_manager.get_event(event.id)
	assert fetched_event != None
	assert fetched_event.id == event.id

	cleanup(event.id)

def test_delete_event():
	event = create_test_event()
	fetched_event = event_manager.get_event(event.id)
	assert fetched_event != None
	event_manager.delete_event(event.id)
	fetched_event = event_manager.get_event(event.id)
	assert fetched_event == None
	
	cleanup(event.id)

def test_update_event_type():
	event = create_test_event()
	assert event.event_type == None
	event_manager.update_event_type(event.id, 'AURA')
	fetched_event = event_manager.get_event(event.id)
	assert fetched_event.event_type == 'AURA'

	cleanup(event.id)

def test_update_event_duration():
	event = create_test_event()
	assert event.event_duration == None
	event_manager.update_event_duration(event.id, 99)
	fetched_event = event_manager.get_event(event.id)
	assert fetched_event.event_duration == 99

	cleanup(event.id)

def test_update_event_severity():
	event = create_test_event()
	assert event.event_severity == None
	event_manager.update_event_severity(event.id, 5)
	fetched_event = event_manager.get_event(event.id)
	assert fetched_event.event_severity == 5

	cleanup(event.id)

def test_update_event_tracking_status_name():
	event = create_test_event()
	assert event.event_tracking_status_name == 'CREATED'

	event_manager.update_event_type(event.id, 'AURA')
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

	cleanup(event.id)



## Helpers

def cleanup(event_id):
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
