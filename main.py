import requests

API_KEY = "YOUR_API_KEY"

city = input("Enter City Name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if data["cod"] != 200:
    print("❌ City not found!")
else:
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)