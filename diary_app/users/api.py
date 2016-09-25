from diary_app import application
from flask import jsonify, request

@application.route('/get_or_create_user', methods=['POST'])
def get_or_create_user():
	username = request.json['username']
	return jsonify( {'user_id' : "FAKE_ID"} )