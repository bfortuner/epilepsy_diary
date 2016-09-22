
import boto
import boto.s3
import sys
from boto.s3.key import Key

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

import random

def createChart(data):
	filename = random.getrandbits(32)
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

	py.image.save_as(fig, filename='graphs/' +str(filename) +'.png')

	s3_connection = boto.connect_s3()
	bucket = s3_connection.get_bucket('hapibot-graph')
	key = boto.s3.key.Key(bucket,str(filename))
	key.set_contents_from_filename('graphs/' +str(filename) +'.png')

	return 'https://hapibot-graph.s3.amazonaws.com/'+str(filename)

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

print createChart(data)


