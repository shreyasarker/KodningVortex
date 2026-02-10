from flask import Flask, render_template, request
import urllib.request
import urllib.parse
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = None

    if request.method == "POST":
        location = request.form.get("location", "").strip()

        try:
            q = urllib.parse.quote(location)
            url = f"https://nominatim.openstreetmap.org/search?q={q}&format=json&limit=1"

            # Nominatim requires a User-Agent
            req = urllib.request.Request(url, headers={"User-Agent": "FlaskMapApp/1.0"})
            source = urllib.request.urlopen(req).read()
            response = json.loads(source)

            if not response:
                error = "Location not found."
            else:
                lat = float(response[0]["lat"])
                lon = float(response[0]["lon"])
                data = {"location": location, "lat": lat, "lon": lon}

        except Exception as e:
            error = f"Error: {e}"

    return render_template("index.html", data=data, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
