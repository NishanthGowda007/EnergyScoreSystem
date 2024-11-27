import random
import pandas as pd

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

num_entries = 100
dataset = generate_dataset(num_entries)

dataset.to_csv("random_health_dataset_with_extra_columns.csv", index=False)

print(dataset)
