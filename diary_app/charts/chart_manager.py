import plotly.plotly as py
import plotly.graph_objs as go
from diary_app.utils import id_generator
from diary_app.clients import s3
from diary_app.config import config
from diary_app.events import event_manager
from diary_app.charts.constants import EVENT_CHART_TITLE, X_LABEL, Y_LABEL
from diary_app.events.constants import SEIZURE_EVENT_TYPE, AURA_EVENT_TYPE
import datetime


def get_chart(username):
    current_time = datetime.datetime.utcnow()
    start_time = current_time - datetime.timedelta(days=30)
    seizure_data = event_manager.get_event_count_in_date_range(
        username, start_time, current_time, SEIZURE_EVENT_TYPE)
    dates = extract_dates_from_events(seizure_data)
    seizure_counts = extract_counts_from_events(seizure_data)

    aura_data = event_manager.get_event_count_in_date_range(
        username, start_time, current_time, AURA_EVENT_TYPE)
    aura_counts = extract_counts_from_events(aura_data)

    chart_data = {
        "title": EVENT_CHART_TITLE,
        "x": {
            'label': X_LABEL,
            'data': {
                'Seizures': dates,
                'Auras': dates
            }
        },
        "y": {
            'label': Y_LABEL,
            'data': {
                'Seizures': seizure_counts,
                'Auras': aura_counts
            }
        },
        'groups': ['Seizures', 'Auras']
    }
    chart_url = build_grouped_bar_chart(chart_data)
    return chart_url


def extract_dates_from_events(events_data):
    dates = []
    for data in events_data:
        dates.append(data[0])
    return dates


def extract_counts_from_events(events_data):
    counts = []
    for data in events_data:
        counts.append(data[1])
    return counts


def build_grouped_bar_chart(chart_data):
    py.sign_in(config.PLOTLY_USERNAME, config.PLOTLY_PASSWORD)
    bars = []
    for name in chart_data['groups']:
        bar = go.Bar(
            x=chart_data["x"]["data"][name],
            y=chart_data["y"]["data"][name],
            name=name
        )
        bars.append(bar)

    chart_layout = dict(title=chart_data['title'],
                        xaxis=dict(title=chart_data['x']['label'],
                            tickangle=-45),
                        yaxis=dict(title=chart_data['y']['label']),
                        width=800,
                        height=640)
    chart = go.Figure(data=bars, layout=chart_layout)
    filename = id_generator.generate_chart_image_filename()
    py.image.save_as(chart, filename=config.LOCAL_CHARTS_DIR_PATH + filename)

    s3.upload_file(filename, config.LOCAL_CHARTS_DIR_PATH +
                   filename, config.S3_USER_CHARTS_BUCKET)
    download_url = s3.get_download_url(
        bucket=config.S3_USER_CHARTS_BUCKET,
        path=filename,
        expiry=603148)

    return download_url
