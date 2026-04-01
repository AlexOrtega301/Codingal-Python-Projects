from flask import Flask, render_template, request
import json
import urllib.request
from urllib.parse import quote

app = Flask(__name__)

def fetch_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", data=None, error=None)

@app.route("/getweather", methods=["POST"])
def weather():
    location = request.form.get("city", "").strip()

    if not location:
        return render_template("index.html", data=None, error="Please enter a city name.")

    try:
        # 1) Get coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={quote(location)}&count=1&language=en&format=json"
        geo_data = fetch_json(geo_url)

        if not geo_data.get("results"):
            return render_template("index.html", data=None, error="City not found.")

        place = geo_data["results"][0]
        lat = place["latitude"]
        lon = place["longitude"]

        city_name = place.get("name", location)
        country_code = place.get("country_code", "").upper()

        # 2) Get weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_data = fetch_json(weather_url)

        current_weather = weather_data.get("current_weather", {})
        temp_c = current_weather.get("temperature")

        data = {
            "location": city_name,
            "country_code": country_code or "N/A",
            "temp": f"{temp_c} °C" if temp_c is not None else "N/A"
        }

        return render_template("index.html", data=data, error=None)

    except Exception as e:
        return render_template("index.html", data=None, error="Something went wrong.")

if __name__ == "__main__":
    app.run(debug=True)