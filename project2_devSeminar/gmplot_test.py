import plotly.plotly as py
from plotly.graph_objs import *

# mapbox_access_token = 'pk.eyJ1IjoicHZvbmxlaCIsImEiOiJjamYxcXgza2swMnhsMzNyejAwaHgydmhiIn0.nXTBJ-ZVvBguCg3r1zZdbg'
#state = input('Enter state ex. MA, CA etc..: ')
city = input('Enter city ex. Brockton, Bridgewater etc..: ')
#request = requests.get('http://api.wunderground.com/api/947737bc6a822a9e/conditions/q/' + state + '/' + city + '.json')
#soup = BeautifulSoup(request.text, "lxml")
data = Data([
    Scattermapbox(
        lat=['45.5017'],
        lon=['-73.5673'],
        mode='markers',
        marker=Marker(
            size=14
        ),
        text=[city],
    )
])

layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken='pk.eyJ1IjoicHZvbmxlaCIsImEiOiJjamYzOHZ6bmswNnkyMnlsdHptYjlkNGM2In0.Eu3jSih10cgvdG-FiYWF4w',

        bearing=0,
        center=dict(
            lat=45,
            lon=-73
        ),
        pitch=0,
        zoom=5
    ),
)

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='test Mapbox')