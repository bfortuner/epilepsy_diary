from diary_app import application
from diary_app.charts import chart_manager
from flask import jsonify


@application.route('/chart/<username>', methods=['GET'])
def get_chart(username):
    chart_url = chart_manager.get_chart(username)
    return jsonify({
        'chart': chart_url
    })
