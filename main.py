import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = input("Enter a city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=imperial"
response = requests.get(url)
data = response.json()
if response.status_code != 200:
    print(f"Couldn't find that city. Error: {data.get('message', 'unknown error')}")
    exit()
city = data["name"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
wind_speed = data["wind"]["speed"]
print(f"Weather in {city}")
print(f"Temperature {temp}°F (Feels like {feels_like}°F)")
print(f"Conditions: {description}")
print(f"Humidity: {humidity}%")
print(f"Wind: {wind_speed} mph")
print("\n5-Day Forecast:")
forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=imperial"
forecast_response = requests.get(forecast_url)
forecast_data = forecast_response.json()
seen_days = set()
for entry in forecast_data["list"]:
    date_time = entry["dt_txt"].split(" ")
    date = date_time[0]
    time = date_time[1]
    if date not in seen_days and time == "12:00:00":
        seen_days.add(date)
        temp = entry["main"]["temp"]
        desc = entry["weather"][0]["description"]
        print(f"{date}: {temp}°F, {desc}")
