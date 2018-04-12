import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDrPDdT4DLxsNQOLSpmzd7VGvOGeKOQLz4')
#first key
#AIzaSyDcZjk6lT9fH_UH0H7h-InyvV-bhDB9va4
#second key
#AIzaSyDrPDdT4DLxsNQOLSpmzd7VGvOGeKOQLz4
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)