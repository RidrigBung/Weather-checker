from flask import Flask, render_template
from get_weather_list import data_list, current_data, max_temps
from get_weather_json import city

app = Flask(__name__)


@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html', city=city["name"], data_list=data_list, current_data=current_data, max_temps=max_temps)


if __name__ == "__main__":
    app.run(debug=True)
