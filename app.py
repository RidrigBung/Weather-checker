from flask import Flask, render_template
from get_weather_list import data_list, today_temp
from get_weather_json import city

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html', city=city["name"], data_list=data_list, today_temp=today_temp)


if __name__ == "__main__":
    app.run(debug=True)
