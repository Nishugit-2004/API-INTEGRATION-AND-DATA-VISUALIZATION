print("Script is running...")

import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
API_KEY = "6694c4779044cbbba8888ef4fb62c0ca"
CITY = "Chennai"
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

# -----------------------------
# FETCH DATA FROM API
# -----------------------------
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code != 200:
    print("Error fetching data:", response.json())
    exit()

data = response.json()

# -----------------------------
# PROCESS DATA
# -----------------------------
weather_list = []

for entry in data["list"]:
    weather_list.append({
        "datetime": datetime.fromtimestamp(entry["dt"]),
        "temperature": entry["main"]["temp"],
        "humidity": entry["main"]["humidity"],
        "pressure": entry["main"]["pressure"],
        "wind_speed": entry["wind"]["speed"]
    })

df = pd.DataFrame(weather_list)

# -----------------------------
# CREATE VISUALIZATION DASHBOARD
# -----------------------------
plt.figure(figsize=(14, 10))

# Temperature
plt.subplot(2, 2, 1)
plt.plot(df["datetime"], df["temperature"])
plt.title("Temperature Forecast")
plt.xticks(rotation=45)

# Humidity
plt.subplot(2, 2, 2)
plt.plot(df["datetime"], df["humidity"])
plt.title("Humidity Forecast")
plt.xticks(rotation=45)

# Pressure
plt.subplot(2, 2, 3)
plt.plot(df["datetime"], df["pressure"])
plt.title("Pressure Forecast")
plt.xticks(rotation=45)

# Wind Speed
plt.subplot(2, 2, 4)
plt.plot(df["datetime"], df["wind_speed"])
plt.title("Wind Speed Forecast")
plt.xticks(rotation=45)

plt.tight_layout()
plt.suptitle(f"5-Day Weather Forecast Dashboard - {CITY}", fontsize=16)
plt.subplots_adjust(top=0.93)

plt.show()
