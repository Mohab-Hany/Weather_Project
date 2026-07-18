import tkinter as tk
import requests
from tkinter import messagebox


# OpenWeatherMap API Key
API_KEY = "1f347a496afab32c2c5047e806b0cd98"


# Get weather data from API
def get_weather():

    city = location_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter a location.")
        return

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        # Check if the city exists
        if str(data.get("cod")) != "200":
            messagebox.showerror("Error", "Location not found.")
            return

        # Get weather information
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"] * 3.6
        pressure = data["main"]["pressure"]

        # Precipitation (if available)
        precipitation = 0

        if "rain" in data:
            precipitation = data["rain"].get("1h", 0)

        # Update labels
        temperature_label.config(
            text=f"Temperature: {temperature:.1f}°C"
        )

        humidity_label.config(
            text=f"Humidity: {humidity}%"
        )

        wind_speed_label.config(
            text=f"Wind Speed: {wind_speed:.1f} km/h"
        )

        pressure_label.config(
            text=f"Pressure: {pressure} hPa"
        )

        precipitation_label.config(
            text=f"Precipitation: {precipitation}%"
        )

    except Exception:
        messagebox.showerror(
            "Error",
            "Something went wrong. Please try again."
        )


# Create the main window
window = tk.Tk()
window.title("Weather Forecast")
window.geometry("600x400")
window.resizable(False, False)


# Location Label
location_label = tk.Label(
    window,
    text="Location:",
    font=("Arial", 16)
)
location_label.place(x=200, y=30)


# Location Entry
location_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=15
)
location_entry.place(x=320, y=35)


# Search Button
search_button = tk.Button(
    window,
    text="Search",
    font=("Arial", 10),
    command=get_weather
)
search_button.place(x=500, y=32)


# Temperature Label
temperature_label = tk.Label(
    window,
    text="Temperature: --",
    font=("Arial", 16)
)
temperature_label.place(x=60, y=100)


# Humidity Label
humidity_label = tk.Label(
    window,
    text="Humidity: --",
    font=("Arial", 16)
)
humidity_label.place(x=60, y=160)


# Wind Speed Label
wind_speed_label = tk.Label(
    window,
    text="Wind Speed: --",
    font=("Arial", 16)
)
wind_speed_label.place(x=60, y=220)


# Pressure Label
pressure_label = tk.Label(
    window,
    text="Pressure: --",
    font=("Arial", 16)
)
pressure_label.place(x=60, y=280)


# Precipitation Label
precipitation_label = tk.Label(
    window,
    text="Precipitation: --",
    font=("Arial", 16)
)
precipitation_label.place(x=60, y=340)


# Start the application
window.mainloop()

