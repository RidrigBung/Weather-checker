import requests
from datetime import date
from typing import Any
from classes import City


def download_weather_json(city: City, cur_date: date) -> Any:
    base_url = "https://api.open-meteo.com/v1/forecast?"

    response = requests.get(
        base_url + f"latitude={city.latitude}&longitude={city.longitude}&hourly=temperature_2m,precipitation_probability,weathercode,surface_pressure,windspeed_10m&timezone=auto")
    # print(f"https get response: {response}")
    return response.json()
