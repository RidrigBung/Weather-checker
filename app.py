from flask import Flask, render_template, url_for, request
from datetime import date
from weather_data_processing import get_current_weather_data
from cities_load import get_cities
from classes import City

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city_name = request.form.get("city_name")
        if city_name == "":
            latitude = request.form.get("latitude")
            longitude = request.form.get("longitude")
            if latitude == "" or longitude == "":
                return render_template('index.html', cities=get_cities())
            city_name = "Coordinates"
            city = City(latitude, longitude, city_name)
            cur_date = date.today()
            data = get_current_weather_data(city, cur_date)
            return render_template('weather.html', city=city.name, today=data["today"], hours=data["hours"], week=data["week"])
        for static_city in get_cities():
            if static_city["name"] == city_name:
                latitude = static_city["latitude"]
                longitude = static_city["longitude"]
                break
        city = City(latitude, longitude, city_name)
        cur_date = date.today()
        data = get_current_weather_data(city, cur_date)
        return render_template('weather.html', city=city.name, today=data["today"], hours=data["hours"], week=data["week"])
    return render_template('index.html', cities=get_cities())


if __name__ == "__main__":
    app.run(debug=True)
