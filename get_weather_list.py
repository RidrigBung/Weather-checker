import json
from datetime import datetime, date


def get_weather_lists(date_times: list = []) -> list:
    weather_date = []
    weather_week_day = []
    week = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    weather_time = []
    for date_time in date_times:
        weather_date.append(date_time[:10])
        weather_week_day.append(
            week[date.fromisoformat(date_time[:10]).weekday()])
        weather_time.append(date_time[11:13])
    return weather_date, weather_week_day, weather_time


def get_weathercode(codes: list = []) -> list:
    weathercode = []
    code_dict = {0: "0", 1: "0", 2: "1", 3: "1", 45: "1",
                 48: "1", 51: "2", 53: "2", 55: "2", 56: "2",
                 57: "2", 61: "2", 63: "2", 65: "2", 66: "2",
                 67: "2", 71: "3", 73: "3", 75: "3", 77: "3",
                 80: "2", 81: "2", 82: "2", 85: "2", 86: "2",
                 95: "2", 96: "2", 99: "2"}
    for code in codes:
        weathercode.append(code_dict[code])
    return weathercode


print(str(datetime.now())[:10])
with open(f"./weather_data/weather {str(datetime.now())[:10]}.json", "r") as file:
    data_string = ""
    for line in file:
        data_string += line.rstrip()
data_dict = json.loads(data_string)

data_dict = data_dict["hourly"]
weather_date, weather_week_day, weather_time = get_weather_lists(
    data_dict["time"])
temperature = data_dict["temperature_2m"]
weathercode = get_weathercode(data_dict["weathercode"])

data_list = list(zip(weather_date, weather_week_day, weather_time, temperature,
                     weathercode))
for d in data_list:
    print(d)

cur_hour, cur_minute = int(str(datetime.now())[11:13]), int(
    str(datetime.now())[14:16])
# print(cur_hour, cur_minute)
if cur_minute >= 30:
    cur_hour += 1
for elem in data_list:
    if int(elem[2]) == cur_hour:
        today_temp = elem[3]
