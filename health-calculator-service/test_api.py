import requests # type: ignore

# Test BMI
bmi_response = requests.post("http://localhost:5000/bmi", json={"height": 1.75, "weight": 70})
print("BMI Response:", bmi_response.json())

# Test BMR
bmr_response = requests.post("http://localhost:5000/bmr", json={"height": 175, "weight": 70, "age": 25, "gender": "male"})
print("BMR Response:", bmr_response.json())
