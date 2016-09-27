from diary_app import application
from diary_app.users import user_manager
from flask import jsonify, request


@application.route('/user/<username>', methods=['GET'])
def get_user(username):
    user = user_manager.get_or_create_user(username)
    return jsonify({
        'user_id': user.id,
        'username': user.username
    })


@application.route('/get_or_create_user', methods=['POST'])
def get_or_create_user():
    username = request.json['username']
    user = user_manager.get_or_create_user(username)
    return jsonify({
        'user_id': user.id,
        'username': user.username
    })
