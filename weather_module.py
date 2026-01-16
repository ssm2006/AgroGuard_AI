import requests
import time
from datetime import datetime

API_KEY = "YOUR_API_KEY"

def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "weather": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    return None

def auto_weather_update(city, interval=600):
    while True:
        weather = get_weather_data(city)
        print("Weather Updated:", weather)
        time.sleep(interval)
