import random
import pandas as pd

def calculate_energy_score(data):
    steps = data["steps"]
    exercise_minutes = data["exercise_minutes"]
    heart_rate_avg = data["heart_rate_avg"]
    stress_level = data["stress_level"]
    total_sleep_time = data["total_sleep_time"]
    sleep_efficiency = data["sleep_efficiency"]
    protein = data["protein"]
    carbohydrates = data["carbohydrates"]
    fat = data["fat"]

    activity_score = (
        min(steps / 10000, 1) * 0.4 +  
        min(exercise_minutes / 60, 1) * 0.4 + 
        (1 if heart_rate_avg in range(60, 100) else 0) * 0.2
    ) * 40 

    nutrition_score = (
        min(protein / 100, 1) * 0.4 +
        min(carbohydrates / 150, 1) * 0.4 +   
        min(fat / 70, 1) * 0.2
    ) * 30  

    sleep_quality = (
        min(total_sleep_time / 480, 1) * 0.5 +
        min(sleep_efficiency / 100, 1) * 0.5
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

    if lifestyle == "lazy":
        energy_score *= 0.8  
    elif lifestyle == "active":
        energy_score *= 1.1  
    elif lifestyle == "highly_active":
        energy_score *= 1.2  

    return round(min(max(energy_score, 0), 100), 2)

def generate_dataset(num_entries):
    data = {
        "id": list(range(1, num_entries + 1)),
        "steps": [random.randint(5000, 15000) for _ in range(num_entries)],
        "exercise_minutes": [random.randint(10, 120) for _ in range(num_entries)],
        "heart_rate_avg": [random.randint(60, 100) for _ in range(num_entries)],
        "stress_level": [random.randint(0, 5) for _ in range(num_entries)],
        "total_sleep_time": [random.randint(300, 600) for _ in range(num_entries)],
        "sleep_efficiency": [random.randint(70, 100) for _ in range(num_entries)],
        "protein": [random.randint(50, 120) for _ in range(num_entries)],
        "carbohydrates": [random.randint(100, 250) for _ in range(num_entries)],
        "fat": [random.randint(40, 120) for _ in range(num_entries)],
        "age": [random.randint(18, 75) for _ in range(num_entries)],
        "gender": [random.choice(["male", "female"]) for _ in range(num_entries)],
        "lifestyle": [random.choice(["lazy", "active", "highly_active"]) for _ in range(num_entries)],
    }
    return pd.DataFrame(data)

def calculate_energy_scores_for_dataset(dataset):
    results = []
    for index, row in dataset.iterrows():
        base_score = calculate_energy_score(row)
        normalized_score = normalize_scores(row["age"], row["gender"], row["lifestyle"], base_score)
        row["normalized_energy_score"] = normalized_score
        results.append(row)
    
    return pd.DataFrame(results)

num_entries = 100
dataset = generate_dataset(num_entries)
dataset_with_scores = calculate_energy_scores_for_dataset(dataset)
dataset_with_scores.to_csv("energy_scores_output.csv", index=False)
print(dataset_with_scores)
