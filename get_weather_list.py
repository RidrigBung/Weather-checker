import json
from datetime import datetime, date


# Разбитие формата {date}T{time} на дату, день недели и час.
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


# Источник json файла даёт множество кодов состояний погоды,
# функция обобщает их до: 0 - ясно, 1 - облачно, 2 - дождь, 3 - снег.
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


# Загрузка данных из последнего json файла в data_dict
with open(f"./weather_data/weather {str(datetime.now())[:10]}.json", "r") as file:
    data_string = ""
    for line in file:
        data_string += line.rstrip()
data_dict = json.loads(data_string)

# Вся полезная информация хранится в словаре, где значения - списки,
# словарь можно получить по ключу "hourly", элементы списка -
# это данные о погоде с разницей во времени 1 час для соседних элементов.
# Списки содержат почасовую информацию о 7 днях начиная с сегодняшнего.
data_dict = data_dict["hourly"]

# Разбитие значений словаря на списки
weather_date, weather_week_day, weather_time = get_weather_lists(
    data_dict["time"])
temperature = data_dict["temperature_2m"]
weathercode = get_weathercode(data_dict["weathercode"])
surface_pressure = data_dict["surface_pressure"]
windspeed_10m = data_dict["windspeed_10m"]

# Объединение полученных выше словарей в единую структуру данных
data_list = list(zip(weather_date, weather_week_day, weather_time, temperature,
                     weathercode, surface_pressure, windspeed_10m))
# for d in data_list:
#     print(d)

# Получение текущей температуры,
# атмосфореного давления и скорости ветра
cur_hour, cur_minute = int(str(datetime.now())[11:13]), int(
    str(datetime.now())[14:16])
if cur_minute >= 30:
    cur_hour += 1
for elem in data_list:
    if int(elem[2]) == cur_hour:
        # temperature, surface_pressure, windspeed_10m
        current_data = [elem[3], elem[5], elem[6]]
