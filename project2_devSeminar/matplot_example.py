import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()


mpis = [{'lat': ['36.7347725'],
  'lon': ['70.8119953'],
  'marker': {'color': 'rgb(0,116,217)',
   'line': {'color': 'rgb(40,40,40)', 'width': 0.5},
   'size': 38.700000000000003,
   'sizemode': 'diameter'},
  'text': '0.387',
  'type': 'scattergeo'},
]


layout = go.Layout(
    title = 'MPI',
    showlegend = True,
    geo = dict(
            scope='world',
            projection=dict( type = 'natural earth'),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),)

fig =  go.Figure(layout=layout, data=mpis)
iplot( fig, validate=False)