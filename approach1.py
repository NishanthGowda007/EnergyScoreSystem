def calculate_energy_score(data):
    steps = data["steps"]
    exercise_minutes = data["exercise_minutes"]
    heart_rate_avg = data["heart_rate_avg"]
    stress_level = data["stress_level"]
    sleep_data = data["sleep_data"]
    nutrients = sleep_data["nutrients"]

    activity_score = (
        min(steps / 10000, 1) * 0.4 +  
        min(exercise_minutes / 60, 1) * 0.4 + 
        (1 if heart_rate_avg in range(60, 100) else 0) * 0.2
    ) * 40 

    calorie_balance = nutrients["protein"] + nutrients["carbohydrates"] + nutrients["fat"]
    nutrition_score = (
        min(nutrients["protein"] / 100, 1) * 0.4 +
        min(nutrients["carbohydrates"] / 150, 1) * 0.4 +   
        min(nutrients["fat"] / 70, 1) * 0.2
    ) * 30  

    sleep_quality = (
        min(sleep_data["total_sleep_time"] / 480, 1) * 0.5 +
        min(sleep_data["sleep_efficiency"] / 100, 1) * 0.5
    ) * 20  

    stress_score = max(0, 10 - stress_level * 2) 

    total_score = activity_score + nutrition_score + sleep_quality + stress_score
    return round(total_score, 2)

def normalize_scores(age, gender, lifestyle, energy_score):
    if age < 30:
        energy_score *= 1.1  
    elif age > 60:
        energy_score *= 0.85  

    if gender == "female":
        energy_score *= 0.95  

    if lifestyle == "sedentary":
        energy_score *= 0.8  
    elif lifestyle == "active":
        energy_score *= 1.1  
    elif lifestyle == "highly_active":
        energy_score *= 1.2  

    return min(max(energy_score, 0), 100)

input_data = {
    "steps": 8000,
    "exercise_minutes": 45,
    "heart_rate_avg": 85,
    "heart_rate_variability_avg": 70,
    "calories_burned": 2500,
    "stress_level": 2,
    "sleep_data": {
        "total_sleep_time": 480,
        "sleep_stages": {
            "rem_sleep": 90,
            "non_rem_sleep": {"light_sleep": 210, "deep_sleep": 120},
            "awake_time": 60
        },
        "sleep_efficiency": 90,
        "time_in_bed": 530,
        "active_sleep": 30,
        "nutrients": {
            "protein": 80,
            "carbohydrates": 120,
            "fat": 80
        }
    },
    "age": 25,
    "gender": "female",
    "lifestyle": "active"
}

base_energy_score = calculate_energy_score(input_data)
normalized_energy_score = normalize_scores(input_data["age"], input_data["gender"], input_data["lifestyle"], base_energy_score)

print(f"Final Normalized Energy Score: {normalized_energy_score}")
