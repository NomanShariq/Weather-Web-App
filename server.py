from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)

# A simulated function to fetch weather data based on the city
def get_current_weather(city):
    # Replace this with actual weather data retrieval logic
    # Simulate weather data as a dictionary for demonstrationdddd
    return {
        "name": city,
        "weather": [{"description": "Sunny"}],
        "main": {"temp": 25.0, "feels_like": 28.0},
        "cod": 200,
    }

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/weather")
def get_weather():
    city = request.args.get("city", "Karachi")  # Use default value if city is not provided

    weather_data = get_current_weather(city)

    if weather_data["cod"] != 200:
        return render_template("city_not_found.html")

    # Capitalize the weather description
    weather_description = weather_data["weather"][0]["description"].capitalize()

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_description,
        temp=f"{weather_data['main']['temp']:.1f}°C",
        feels_like=f"{weather_data['main']['feels_like']}°C",
    )

if __name__ == "__main__":
    # Use 'waitress' to serve the application on host 0.0.0.0 and port 5000
    serve(app, host="0.0.0.0", port=5000)
