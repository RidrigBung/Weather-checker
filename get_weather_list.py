import json
from datetime import datetime, date


def get_weather_date_and_time(date_times: list = []) -> list:
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


with open("./weather_data/weather 2023-07-27.json", "r") as file:
    data_string = ""
    for line in file:
        data_string += line.rstrip()
data_dict = json.loads(data_string)

data_dict = data_dict["hourly"]
weather_date, weather_week_day, weather_time = get_weather_date_and_time(
    data_dict["time"])
temperature = data_dict["temperature_2m"]
weathercode = data_dict["weathercode"]
precipitation_probability = data_dict["precipitation_probability"]

data_list = list(zip(weather_date, weather_week_day, weather_time, temperature,
                     weathercode, precipitation_probability))
# for d in data_list:
#     print(d)

cur_hour, cur_minute = int(str(datetime.now())[11:13]), int(
    str(datetime.now())[14:16])
# print(cur_hour, cur_minute)
if cur_minute >= 30:
    cur_hour += 1
for elem in data_list:
    if int(elem[2]) == cur_hour:
        today_temp = elem[3]
