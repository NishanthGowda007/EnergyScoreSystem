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

dataset = pd.read_csv("synthetic_health_data1.csv")

def calculate_energy_scores_for_dataset(dataset):
    results = []
    for index, row in dataset.iterrows():
        base_score = calculate_energy_score(row)
        normalized_score = normalize_scores(row["age"], row["gender"], row["lifestyle"], base_score)
        row["normalized_energy_score"] = normalized_score
        results.append(row)
    
    return pd.DataFrame(results)

dataset_with_scores = calculate_energy_scores_for_dataset(dataset)

dataset_with_scores.to_csv("energy_scores_output.csv", index=False)

print(dataset_with_scores)
