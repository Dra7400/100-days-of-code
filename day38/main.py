from datetime import datetime
import requests


GENDER = "male"
WEIGHT_KG = "90"
HEIGHT_CM = "177"
AGE = "47"

APP_ID = "4dbfde2d"
API_KEY = "43d8b73d48b12b89bdf5b0bd27dcf689"
TOKEN = "Cricket0404!"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ce33c06ed6227d004580b7b91266772e/workoutTracking/workouts"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m%Y")
now_time = datetime.now().strftime("%X")


#
#
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
#
bearer_headers = {
    "Authorization": f"Bearer {TOKEN}"
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
