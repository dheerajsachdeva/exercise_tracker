APP_ID = "6b04fb4e"
API_KEY = "42dab3a7fd450122fc56de9c6c7b38eb"
HEIGHT = 167.64
WEIGHT = 72.5
AGE = 30
GENDER = "male"
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

import requests
from datetime import datetime

user_query = input("Tell which exercise you did?")

headers = {
 "x-app-id": APP_ID,
 "x-app-key": API_KEY,
 "Content-Type": "application/json"
}

parameters = {
 "query": user_query,
 "gender": GENDER,
 "weight_kg": WEIGHT,
 "height_cm": HEIGHT,
 "age": AGE
}

response = requests.post(url=API_ENDPOINT, headers=headers, json=parameters)
result = response.json()
print(result)

# Sheet codes:
sheet_endpoint = "https://api.sheety.co/fe578fbd6696f897057157e46f7b780f/myWorkouts/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")

sheet_headers = {
 "Content-Type": "application/json",
}
for exercise in result["exercises"]:
    sheet_params = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, headers=sheet_headers, json=sheet_params)
    print(sheet_response.text)


