# Energy Score System

## Project Purpose
The Energy Score System is a tool to calculate a person's energy score based on key factors like physical activity, nutrition, sleep, and stress levels. This score helps users track their overall health and make informed decisions to improve their well-being.

## How to Run the Code
1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/energy-score-system.git
   ```
3. Navigate to the project folder:
   ```bash
   cd energy-score-system
   ```
4. Run the Python script:
   ```bash
   python energy_score.py
   ```

## Example Input and Output
**Input:**
```json
{
  "steps": 10000,
  "exercise_minutes": 45,
  "heart_rate_avg": 85,
  "heart_rate_variability_avg": 70,
  "calories_burned": 2500,
  "stress_level": 2,
  "sleep_data": {
    "total_sleep_time": 480,
    "sleep_stages": {
      "rem_sleep": 90,
      "non_rem_sleep": {
        "light_sleep": 210,
        "deep_sleep": 120
      },
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
  }
}
