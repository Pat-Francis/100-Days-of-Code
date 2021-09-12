import os
import requests
import datetime

GENDER = "Male"
WEIGHT_KG = os.getenv("MY_WEIGHT")
HEIGHT_CM = os.getenv("MY_HEIGHT")
AGE = os.getenv("MY_AGE")

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/b0067220fed41902ba9a2c6cbfe1f147/workoutTracking/workouts"
SHEET_KEY = os.getenv("SHEET_KEY")

# NutritionIX API setup and request
exercise_text = input("Please enter the exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0",
}

exercise_parameters = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(url=EXERCISE_URL, json=exercise_parameters, headers=headers)
response_data = response.json()

# Sheet API setup and request
today_date = datetime.datetime.today().strftime("%d/%m/%Y")
time_now = datetime.datetime.today().strftime("%H:%M:%S")

for exercise in response_data["exercises"]:
    sheet_parameters = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_headers = {
    "Authorization": f"Bearer {SHEET_KEY}",
    "Content-Type": "application/json"
}

sheet_response = requests.post(url=SHEET_URL, json=sheet_parameters, headers=sheet_headers)

print(sheet_response.text)
