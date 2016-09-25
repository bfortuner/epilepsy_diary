from diary_app import application
from flask import jsonify, request

@application.route('/plugins', methods=['GET'])
def get_job_type_plugins():
	return jsonify({
		'job_types' : "hey",
		'job_type_plugins' : "there",
		'plugins' : "mister"
	})