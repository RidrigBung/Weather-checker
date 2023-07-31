from flask import Flask, render_template, url_for, request
from datetime import date
from get_weather_variables import get_all_weather_data
from classes import City

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = City(request.form.get("latitude"), request.form.get(
            "longitude"), request.form.get("name"))
        cur_date = date.today()
        data = get_all_weather_data(city, cur_date)
        return render_template('weather.html', city=city.name, today=data["today"], hours=data["hours"], week=data["week"])
    return render_template('index.html')


# @app.route("/weather")
# def weather():
#     return render_template('weather.html', city=city.name, today=today, hours=hours, week=week)


if __name__ == "__main__":
    app.run(debug=True)
