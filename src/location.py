import sys
sys.path.append("../")
import requests
from urllib.parse import quote
from credentials.creds import *

class LocationWeather:
    """
    Represents the weather for a given location.
    """
    def __init__(self, address):
        address = quote(address)
        geo_req = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={geocoder_key}"
        geocode = requests.get(geo_req).json()
        self.lat = geocode['results'][0]['geometry']['location']['lat']
        self.lng = geocode['results'][0]['geometry']['location']['lng']

        weather_req = f"https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lng}&units=imperial&appid={weather_key}"
        self.weather = requests.get(weather_req).json()

    def get_temp(self, day):
        return self.weather['daily'][day]['temp']
    
    def get_weather(self, day):
        return self.weather['daily'][day]['weather']

    def get_POP(self, day):
        # POP = Probability of Precipication
        return self.weather['daily'][day]['pop']