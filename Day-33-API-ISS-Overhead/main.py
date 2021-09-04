import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.61814180079598
MY_LONG = 0.5378572981686531
MY_EMAIL = "email@gmail.com"
MY_PASSWORD = "password1234"


def check_if_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LAT <= iss_longitude + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if sunrise_hour >= hour_now >= sunset_hour:
        return True


while True:
    if check_if_overhead() and is_night():
        # Send email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:ISS is visible!\n\nIs it a bird?  Is it a plane!?  No!  It's the ISS!"
                                )
        print("Email sent")
    else:
        print("ISS not visible from current location:")
        print(f"Latitude: {MY_LAT}\nLongitude: {MY_LONG}")

    time.sleep(60)
