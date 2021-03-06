import datetime
from diary_app import application
from flask import jsonify, request
from diary_app.events import event_manager
from diary_app.users import user_manager
from diary_app.auth.authentication import requires_auth


@application.route('/event/<event_id>', methods=['GET'])
@requires_auth
def get_event(event_id):
    event = event_manager.get_event(event_id)
    response = jsonify(
        event_id=event.id,
        user_internal_id=event.user_id,
        event_time=event.event_time,
        event_type=event.event_type,
        event_duration=event.event_duration,
        event_tracking_status=event.event_tracking_status_name
    )
    print response.data
    return response


@application.route('/event/create', methods=['POST'])
@requires_auth
def create_event():
    json = request.get_json()
    print "received request " + str(json)
    username = json['username']
    event_time = datetime.datetime.utcnow()
    user = user_manager.get_or_create_user(username)
    event = event_manager.create_event(user.id, event_time)
    response = jsonify(
        user_internal_id=user.id,
        user_external_id=user.username,
        event_id=event.id
    )
    return response


@application.route('/event/update', methods=['POST'])
@requires_auth
def update_event():
	json = request.get_json()
	print "received request " + str(json)
	event_id = json['event_id']
	event = event_manager.get_event(event_id)
	event.event_type = request.json['event_type']
	event.event_duration = request.json['event_duration']
	event_manager.update_event(event)
	event_manager.update_event_tracking_status(event_id)
	return jsonify(
		event_id=event_id
	)
