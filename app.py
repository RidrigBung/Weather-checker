from flask import Flask, render_template, url_for
from get_weather_variables import today, hours, week
from get_weather_json import city

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', weather_url=url_for("weather"))


@app.route("/weather")
def weather():
    return render_template('weather.html', city=city["name"], today=today, hours=hours, week=week)


if __name__ == "__main__":
    app.run(debug=True)
