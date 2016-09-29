import datetime
from diary_app import application
from flask import jsonify, request
from diary_app.events import event_manager
from diary_app.users import user_manager


@application.route('/event/<event_id>', methods=['GET'])
def get_event(event_id):
	event = event_manager.get_event(event_id)
	return jsonify({
		'event_id': event.id,
		'user_internal_id': event.user_id,
		'event_time': event.event_time,
		'event_type': event.event_type,
		'event_duration': event.event_duration,
		'event_tracking_status': event.event_tracking_status_name
	})


@application.route('/event/create', methods=['POST'])
def create_event():
	print "creating event"
	username = request.json['username']
	event_time = datetime.datetime.utcnow()
	user = user_manager.get_or_create_user(username)
	event = event_manager.create_event(user.id, event_time)
	return jsonify({
		'request_status': 'OK',
		'user_internal_id': user.id,
		'user_external_id': user.username,
		'event_id': event.id
	})


@application.route('/event/update', methods=['POST'])
def update_event():
	print request.json['event_id']
	event_id = request.json['event_id']
	event = event_manager.get_event(event_id)
	event.event_type = request.json['event_type']
	event.event_duration = request.json['event_duration']
	event_manager.update_event(event)
	event_manager.update_event_tracking_status(event_id)
	return jsonify({
		'request_status': 'OK'
	})
