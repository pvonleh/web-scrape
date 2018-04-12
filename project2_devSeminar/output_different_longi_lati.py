import plotly.plotly as py
from plotly.graph_objs import *
import requests
from geopy.geocoders import Nominatim
from bs4 import BeautifulSoup, NavigableString
geolocator = Nominatim()
# location = geolocator.geocode("Chicago Illinois")
# print(location.address)

# city = input('Enter city ex. Brockton, Bridgewater etc..: ')
# state = input('Enter state ex. MA, CA etc..: ')
# miles = input('Enter distance(in miles) ex. 1, 15, 10 etc..:')

# address  = city +', '+state
address = 'Brockton, MA'
location = geolocator.geocode(address)
print(location)

# request = requests.get(
#     'https://stackoverflow.com/jobs/feed?l=Brockton%2c+MA%2c+United+States&u=Miles&d=50')
# soup = BeautifulSoup(request.text, "lxml")
#
# items = soup.find_all('item')
# for item in items:
#     title = item.find('title').text
#     print(title)
