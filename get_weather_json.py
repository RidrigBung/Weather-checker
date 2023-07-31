import requests
from datetime import date
import json


class City:
    latitude: float
    longitude: float
    name: str

    def __init__(self, latitude: float, longitude: float, name: str) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.name = name


base_url = "https://api.open-meteo.com/v1/forecast?"

# city = {"name": "Dmitrov", "latitude": "56.34",
#         "longitude": "37.52", "timezone": "Europe%2FMoscow"}
city = City(56.34, 37.52, "Dmitrov")

response = requests.get(
    base_url + f"latitude={city.latitude}&longitude={city.longitude}&hourly=temperature_2m,precipitation_probability,weathercode,surface_pressure,windspeed_10m&timezone=auto")
print(f"https get response: {response}")
weather_dict = response.json()

with open(f"./weather_data/weather {str(date.today())}.json", "w") as weather_file:
    json.dump(weather_dict, weather_file, sort_keys=True, indent=4)
