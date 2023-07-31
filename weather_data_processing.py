import json
from datetime import datetime, date
from classes import City
from typing import Dict
from get_weather_json import download_weather_json


# Получение названий семи дней недели начиная с сегодня
def get_weather_week_day(date_times: list = []) -> list:
    weather_week_day = []
    week = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    for i in range(0, 7):
        weather_week_day.append(
            week[date.fromisoformat(date_times[i * 24][:10]).weekday()])
    return weather_week_day


# Возвращает время в часах [00:00, 01:00, 02:00, ... ,24:00]
def get_weather_time(date_times: list = []) -> list:
    weather_time = []
    for date_time in date_times[:24]:
        weather_time.append(date_time[11:16])
    return weather_time


# Поиск максимальной температуры в каждый из дней
def get_max_temperature_list(temperatures: dict) -> list:
    max_temperature = []
    for i in range(1, 7):
        max_temperature.append(max(temperatures[i * 24:(i + 1) * 24]))
    return max_temperature


# Возвращает текущий час
def get_cur_hour() -> int:
    cur_hour, cur_minute = int(str(datetime.now())[11:13]), int(
        str(datetime.now())[14:16])
    if cur_minute >= 30:
        cur_hour += 1
    return cur_hour


# Источник json файла даёт множество кодов состояний погоды,
# функция обобщает их до: 0 - ясно, 1 - облачно, 2 - дождь, 3 - снег.
def simplify_weathercode(code_old: int) -> str:
    code_dict = {0: "0", 1: "0", 2: "1", 3: "1", 45: "1",
                 48: "1", 51: "2", 53: "2", 55: "2", 56: "2",
                 57: "2", 61: "2", 63: "2", 65: "2", 66: "2",
                 67: "2", 71: "3", 73: "3", 75: "3", 77: "3",
                 80: "2", 81: "2", 82: "2", 85: "2", 86: "2",
                 95: "2", 96: "2", 99: "2"}
    return code_dict[code_old]


def get_weathercode(codes: list = []) -> list:
    raw_weathercode = []
    for i in range(1, 7):
        raw_weathercode.append(simplify_weathercode(codes[i * 24]))

    return raw_weathercode


def get_current_weather_data(city: City, cur_date: date) -> Dict[str, dict]:
    data_dict = download_weather_json(city, cur_date)

    # Вся полезная информация хранится в словаре, где значения - списки,
    # словарь можно получить по ключу "hourly", элементы списка -
    # это данные о погоде с разницей во времени 1 час для соседних элементов.
    # Списки содержат почасовую информацию о 7 днях начиная с сегодняшнего.
    data_dict = data_dict["hourly"]

    cur_hour = get_cur_hour()
    weather_week_day = get_weather_week_day(data_dict["time"])

    data = {}
    data["today"] = {"temperature": data_dict["temperature_2m"][cur_hour],
                     "weathercode": simplify_weathercode(data_dict["weathercode"][cur_hour]),
                     "week_day": weather_week_day[0],
                     "pressure": data_dict["surface_pressure"][cur_hour],
                     "windspeed": data_dict["windspeed_10m"][cur_hour], }

    data["hours"] = {"time": get_weather_time(),
                     "temperature": data_dict["temperature_2m"][:24]}

    data["week"] = {"temperature": get_max_temperature_list(data_dict["temperature_2m"]),
                    "weathercode": get_weathercode(data_dict["weathercode"]),
                    "week_day": weather_week_day[1:], }

    return data
