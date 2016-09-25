import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

from diary_app.utils import id_generator
from diary_app.clients import s3

CHARTS_DIR_PATH="graphs/"
CHARTS_S3_BUCKET="hapibot-graph"

def create_chart(input_data):
	py.sign_in('hapibot', 'ix1yikrn67') # Replace the username, and API key with your credentials.
	seizures = go.Scatter(
	    x=input_data["x"]["data"],
	    y=input_data["y"]["data"],
	    fill='tozeroy'
	)
	chart_data=[seizures]
	chart_layout = dict(title = 'Seizures (Last 7 Days)',
              xaxis = dict(title = input_data["x"]["label"]),
              yaxis = dict(title = input_data["y"]["label"]),
              width=800, 
              height=640)
	chart = go.Figure(data=chart_data, layout=chart_layout)
	filename = id_generator.generate_chart_image_filename()
	py.image.save_as(chart, filename=CHARTS_DIR_PATH+filename)

	s3.upload_file(filename, CHARTS_DIR_PATH+filename, CHARTS_S3_BUCKET)
	download_url = s3.get_download_url(bucket=CHARTS_S3_BUCKET, path=filename, expiry=603148) #7 days
	
	return download_url


#Test 

data = {
    "x" : {
      'label': "Date",
      'data': ["Sep 22", "Sep 23", "Sep 24", "Sep 25", "Sep 26", "Sep 27", "Sep 28"]
    },
    "y" : {
      'label': "Count",
      'data': [1,3,2,6,3,2,7]
    }
}

if __name__ == "__main__":
	print create_chart(data)


