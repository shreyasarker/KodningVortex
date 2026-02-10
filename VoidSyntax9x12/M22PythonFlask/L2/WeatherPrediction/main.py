from flask import Flask, render_template, request
import json
import urllib.request
import urllib.parse

app = Flask(__name__)

API_KEY = "0a03fe8a9fb0f7576e5f385a97b1ac4c"   # <-- put your real key here

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/getweather", methods=["GET", "POST"])
def getweather():
    city = request.form.get("city", "").strip() if request.method == "POST" else "Chennai"

    if not city:
        return render_template("index.html", error="Please enter a city name.")

    try:
        city_encoded = urllib.parse.quote(city)

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={API_KEY}&units=metric"
        source = urllib.request.urlopen(url).read()
        response_data = json.loads(source)

        # If API returns error like {"cod":"401","message":"Invalid API key"}
        if str(response_data.get("cod")) != "200":
            return render_template("index.html", error=f"API Error: {response_data.get('message')}")

        data = {
            "location": response_data["name"],
            "country_code": response_data["sys"]["country"],
            "temp": response_data["main"]["temp"],
            "condition": response_data["weather"][0]["main"],
        }

        return render_template("index.html", data=data)

    except Exception as e:
        return render_template("index.html", error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
