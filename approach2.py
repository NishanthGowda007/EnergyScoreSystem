import pandas as pd

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


dataset = pd.read_csv("synthetic_health_data1.csv")

def calculate_energy_score_row(row):
    input_data = {
        "steps": row["steps"],
        "exercise_minutes": row["exercise_minutes"],
        "heart_rate_avg": row["heart_rate_avg"],
        "stress_level": row["stress_level"],
        "sleep_data": {
            "total_sleep_time": row["total_sleep_time"],
            "sleep_efficiency": row["sleep_efficiency"],
            "nutrients": {
                "protein": row["protein"],
                "carbohydrates": row["carbohydrates"],
                "fat": row["fat"]
            }
        }
    }
    return calculate_energy_score(input_data)

dataset["energy_score"] = dataset.apply(calculate_energy_score_row, axis=1)

dataset.to_csv("energy_score_results1.csv", index=False)

print("Energy scores calculated and saved to 'energy_score_results1.csv'")