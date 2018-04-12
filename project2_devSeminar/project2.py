import plotly.plotly as py
from plotly.graph_objs import *
import requests
from geopy.geocoders import Nominatim
geolocator = Nominatim()
# location = geolocator.geocode("Chicago Illinois")
# print(location.address)

# city = input('Enter city ex. Brockton, Bridgewater etc..: ')
# state = input('Enter state ex. MA, CA etc..: ')

address = 'BROCKTON, MA'
#address  = city +', '+state
location = geolocator.geocode(address)

#address = "Brockton, MA"
api_key = "AIzaSyBbSXI4rGRgJpeSQjtNw4MV02hjfObjBLQ"
api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
api_response_dict = api_response.json()

if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    # print('Latitude:', latitude)
    # print('Longitude:', longitude)


    latStr = str(latitude) #convert latitude into string
    lonStr = str(longitude)

    tempLat = latStr[:2]
    tempLong = lonStr[:3]

    data = Data([
        Scattermapbox(
            lat=[float(latitude)],
            lon=[float(longitude)],
            mode='markers',
            marker=Marker(
                size=14
            ),
            text=['BROCKTON'],
        )
    ])

    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken='pk.eyJ1IjoicHZvbmxlaCIsImEiOiJjamYzOHZ6bmswNnkyMnlsdHptYjlkNGM2In0.Eu3jSih10cgvdG-FiYWF4w',
            #pk.eyJ1IjoicHZvbmxlaCIsImEiOiJjamYzOHZ6bmswNnkyMnlsdHptYjlkNGM2In0.Eu3jSih10cgvdG - FiYWF4w

    bearing=0,
            center=dict(

                lat=float(tempLat),
                lon=float(tempLong)
            ),
            pitch=0,
            zoom=5
        ),
    )

    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename='Stackoverflow Jobs')

print(location.address)