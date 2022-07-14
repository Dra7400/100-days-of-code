import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "df598b73222d1f5aabaff44a0196c419"

weather_params = {
    "lat": "44.05",
    "lon": "-123.08",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)