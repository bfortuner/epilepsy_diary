import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

from diary_app.utils import id_generator
from diary_app.clients import s3

CHARTS_DIR_PATH="graphs/"
CHARTS_S3_BUCKET="hapibot-graph"


def createChart(data):
	filename = id_generator.generate_chart_image_filename()
	py.sign_in('hapibot', 'ix1yikrn67') # Replace the username, and API key with your credentials.

	x = []
	Seizures = go.Scatter(
	    x=[1, 2, 3, 4],
	    y=[0, 2, 3, 5],
	    fill='tozeroy'
	)

	data=[Seizures]
	layout = go.Layout(title='Seizures', width=800, height=640)
	fig = go.Figure(data=data, layout=layout)

	py.image.save_as(fig, filename=CHARTS_DIR_PATH+filename)
	# conn = s3.get_connection()
	s3.upload_file(filename, CHARTS_DIR_PATH+filename, CHARTS_S3_BUCKET)

	download_url = s3.get_download_url(bucket=CHARTS_S3_BUCKET, path=filename, expiry=603148) #7 days
	return download_url

data = [
    {
      'date': '02-10-2016',
      'count': 3
    },
    {
      'date': '02-11-2016',
      'count': 5
    }
]

if __name__ == "__main__":
	print createChart(data)


