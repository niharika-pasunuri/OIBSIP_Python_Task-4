import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

# Replace with your actual API key
API_KEY = "3f2f3a3555e0245bab6dc45fa09b572b"

# Emoji icons for weather conditions
WEATHER_EMOJIS = {
    "Clear": "☀️",      # ☀️
    "Clouds": "☁️",     # ☁️
    "Rain": "🌧️",   # 🌧️
    "Drizzle": "🌦️", # 🌦🌧️
    "Thunderstorm": "⛈️", # ⛈️
    "Snow": "❄️",       # ❄️
    "Mist": "🌫️",    # 🌫️
}

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            raise ValueError("City not found.")

        temp_c = data["main"]["temp"]
        temp_f = round((temp_c * 9/5) + 32, 2)
        condition = data["weather"][0]["main"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        emoji = WEATHER_EMOJIS.get(condition, "")

        result = (
            f"Weather in {city.title()} {emoji}\n"
            f"Temperature: {temp_c} °C / {temp_f} °F\n"
            f"Condition: {description}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        result_label.config(text=result)
    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve weather data.\n{e}")

# GUI setup
app = tk.Tk()
app.title("Weather ☀️ App - Colorful & Smart")
app.geometry("500x400")
app.config(bg="#d0f0fd")

# Title
tk.Label(app, text="🌤Weather Forecast️", font=("Segoe UI", 20, "bold"), bg="#d0f0fd", fg="#003366").pack(pady=20)

# City input
tk.Label(app, text="Enter City:", font=("Segoe UI", 14), bg="#d0f0fd").pack()
city_entry = tk.Entry(app, font=("Segoe UI", 14), justify='center', width=25)
city_entry.pack(pady=10)

# Button
tk.Button(app, text="Check Weather", font=("Segoe UI", 14, "bold"), bg="#007acc", fg="white", command=get_weather).pack(pady=10)

# Result
result_label = tk.Label(app, text="", font=("Segoe UI", 13), bg="#e6f7ff", fg="#003366", justify="left")
result_label.pack(pady=20, fill="both", expand=True)

app.mainloop()
