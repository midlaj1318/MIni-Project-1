from tkinter import *
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

root = Tk()
def get_weather():

    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()
    if data["cod"] != 200:

        temp_label.config(text="City not found")
        humidity_label.config(text="")
        condition_label.config(text="")

        return

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    temp_label.config(
    text=f"Temperature: {temperature} °C"
    )

    humidity_label.config(
    text=f"Humidity: {humidity} %"
    )

    condition_label.config(
    text=f"Condition: {condition}"
    )

root.title("Weather Dashboard")
root.geometry("500x400")

# Title
title_label = Label(
    root,
    text="🌦 Weather Dashboard",
    font=("Arial", 22, "bold"),
    bg="#EAF4FC",
    fg="#1F4E79"
)
title_label.pack(pady=20)

# City Input
city_entry = Entry(
    root,
    width=25,
    font=("Arial", 14),
    justify="center"
)
city_entry.pack(pady=10)

# Search Button
search_button = Button(
    root,
    text="🔍 Get Weather",
    command=get_weather,
    font=("Arial", 11, "bold"),
    bg="#1F77B4",
    fg="white",
    padx=10,
    pady=5
)
search_button.pack(pady=20)

# Result Labels
temp_label = Label(
    root,
    text="Temperature: -- °C",
    font=("Arial", 14, "bold"),
    bg="#EAF4FC"
)
temp_label.pack(pady=5)

humidity_label = Label(
    root,
    text="Humidity: -- %",
    font=("Arial", 14),
    bg="#EAF4FC"
)
humidity_label.pack(pady=5)

condition_label = Label(
    root,
    text="Condition: --",
    font=("Arial", 14),
    bg="#EAF4FC"
)
condition_label.pack(pady=5)

footer = Label(
    root,
    text="Created by Muhammed Midlaj NK",
    font=("Arial", 9),
    bg="#EAF4FC",
    fg="gray"
)

footer.pack(side="bottom", pady=10)

root.mainloop()