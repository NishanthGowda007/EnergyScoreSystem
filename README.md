# Energy Score System

## Project Purpose
This project calculates an "energy score" based on input data such as physical activity, nutrition, sleep quality, and mental stress levels. The energy score helps users understand their overall health and well-being.

## How to Run the Code
There are two different approaches to calculate the energy score in this repository. Below are the steps to run each approach.
### Approach 1: Basic Energy Score Calculation (Single Input)

This approach calculates the energy score using basic parameters such as steps, exercise minutes, average heart rate, and stress level. It uses a single set of input data for the calculation.

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/NishanthGowda007/EnergyScoreSystem.git
   
2.Navigate to the project folder:
   cd EnergyScoreSystem

3.Run the Python script for Approach 1:
   python approach1.py

### Approach 2: Energy Score Calculation with Dataset
In this approach, the energy score is calculated for each row of health data from a CSV file. This method processes a dataset that includes multiple health records and saves the energy score results to a new CSV file.

1.Clone the repository to your local machine:
    ```bash
 git clone https://github.com/NishanthGowda007/EnergyScoreSystem.git
   
2.Prepare a CSV file (synthetic_health_data1.csv) with health data, including columns such as steps, exercise_minutes, heart_rate_avg, stress_level, total_sleep_time, sleep_efficiency, protein, carbohydrates, and fat.

Place the CSV file in the project directory.

Navigate to the project folder:

bash
Copy code
cd EnergyScoreSystem
Run the Python script for Approach 2:

bash
Copy code
python approach2.py
The energy score for each row in the dataset will be calculated and saved in a new file called energy_score_results1.csv
