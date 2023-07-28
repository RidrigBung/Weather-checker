from flask import Flask, render_template
from get_weather_variables import today, hours, week
from get_weather_json import city

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html', city=city["name"], today=today, hours=hours, week=week)


if __name__ == "__main__":
    app.run(debug=True)
