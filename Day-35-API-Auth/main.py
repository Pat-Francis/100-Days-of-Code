import requests
import smtplib
import os

api_key = os.environ.get("OWM_API_KEY")
my_email = os.environ.get("MY_EMAIL")
my_email_password = os.environ.get("MY_EMAIL_PASSWORD")
receiving_email = os.environ.get("RECEIVING_EMAIL")

parameters = {
    "lat": 51.618147696702735,
    "lon": 0.5378384174799539,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

weather_response = requests.get(url="http://api.openweathermap.org/data/2.5/onecall", params=parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour in weather_slice:
    weather_id = hour["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella!")

    # Send email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_email_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiving_email,
                            msg=f"Subject:Rain expected!\n\nBring an umbrella."
                            )
