import requests

api_key = "9d17f234129767aaebdefe043efb5867"

parameters = {
    "lat": 51.618147696702735,
    "lon": 0.5378384174799539,
    "appid": api_key
}

weather_response = requests.get(url="http://api.openweathermap.org/data/2.5/onecall", params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()

print(weather_response.status_code)
print(weather_data["hourly"])
