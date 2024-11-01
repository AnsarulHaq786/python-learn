import requests
import pandas as pd
import time
from datetime import datetime

locations = [
    {
        "city": "Kathmandu",
        "latitude": 27.7172,
        "longitude": 85.3240},
    {
        "city": "Pokhara",
        "latitude": 28.2096,
        "longitude": 83.9856}
]

weather_data = {
    "Kathmandu": [],
    "Pokhara": []
}

url = "https://api.open-meteo.com/v1/forecast"

def get_weather(location):
    params = {
        "latitude": location["latitude"],
        "longitude": location["longitude"],
        "current_weather": "true"
    }

    response = requests.get(url, params)
    
    if response.status_code == 200:
        data = response.json().get("current_weather")
        if data:
            data["city"] = location["city"]
            data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            city_name = location["city"]
            weather_data[city_name].append(data)
            print("Data fetched!")
    else:
        print(f"Failed to fetch data!")

def save_data_to_csv():
    for city, data in weather_data.items():
        df = pd.DataFrame(data)
        df.to_csv(f"weather_data_,{city.lower()}.csv", index=False)
        print(f"Data saved to weather_data_,{city.lower()}.csv")

try:
    for i in range(15):
        for location in locations:
            get_weather(location)
            save_data_to_csv()
            time.sleep(5)
except KeyboardInterrupt:
    print("\nData collection stopped.")
    save_data_to_csv()
    print("data saved!")