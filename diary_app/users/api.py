from diary_app import application
from diary_app.users import user_manager
from flask import jsonify, request
from diary_app.auth.authentication import requires_auth


@application.route('/user/<username>', methods=['GET'])
@requires_auth
def get_user(username):
    user = user_manager.get_or_create_user(username)
    return jsonify({
        'user_id': user.id,
        'username': user.username
    })


@application.route('/get_or_create_user', methods=['POST'])
@requires_auth
def get_or_create_user():
    username = request.json['username']
    user = user_manager.get_or_create_user(username)
    return jsonify({
        'user_id': user.id,
        'username': user.username
    })
