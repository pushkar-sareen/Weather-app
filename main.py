import requests
from twilio.rest import Client

account_sid = 'Kindly place your sid'
auth_token = 'kindly place your auth token'




api_key = 'kindly place your api key'
OWM_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
weather_params = {
    'lat': 'put your location (int)',
    'lon': 'put your location (int)',
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(url=OWM_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
print(data)


will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("rain")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='place your twilio number',
        body='Its Going To Rain today, remember to bring an umbrella',
        to='place your number'
    )
    print(message.status)