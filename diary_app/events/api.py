from diary_app import application
from flask import jsonify, request

@application.route('/event/<event_id>', methods=['GET'])
def get_event(event_id):
	print event_id
	return jsonify({
		'event_id' : event_id,
		'event_type' : "seizure",
		'duration' : 5,
		'severity' : 2
	})