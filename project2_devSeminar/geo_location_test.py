
import requests
from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("Chicago Illinois")
print(location.address)


address = "Brockton, MA"
api_key = "AIzaSyBbSXI4rGRgJpeSQjtNw4MV02hjfObjBLQ"
api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
api_response_dict = api_response.json()

if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    print('Latitude:', latitude)
    print('Longitude:', longitude)