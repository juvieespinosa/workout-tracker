import requests
from datetime import datetime

APP_ID = "YOUR OWN API"
API_KEY = "SECRET-KEY"
GENDER = "Female"
WEIGHT_KG = 58.98
HEIGHT_CM = 152.40
AGE = 32


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/9f2c335131ed7fcd26ee1051e7cda7b2/workoutTracking/workouts"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

response = requests.post(url=exercise_endpoint, json=exercise_parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": "Bearer LEARNINGCODE101"
    }
    sheety_response = requests.post(
        sheety_endpoint,
        json=sheety_inputs,
        headers=bearer_headers
    )

    print(sheety_response.text)


