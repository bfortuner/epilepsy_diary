from diary_app import application
from diary_app.charts import chart_manager
from flask import jsonify
from diary_app.auth.authentication import requires_auth


@application.route('/chart/<username>', methods=['GET'])
@requires_auth
def get_chart(username):
    chart_url = chart_manager.get_chart(username)
    return jsonify({
        'chart_url': chart_url
    })
