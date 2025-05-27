import pandas as pd
import random

def generate_diabetes_data(n=200):
    data = {
        "Glucose": [random.randint(70, 180) for _ in range(n)],
        "BloodPressure": [random.randint(50, 100) for _ in range(n)],
        "BMI": [round(random.uniform(18.0, 50.0), 1) for _ in range(n)],
        "Age": [random.randint(18, 70) for _ in range(n)],
        "Insulin": [random.randint(50, 250) for _ in range(n)],
        "Outcome": [random.choice([0, 1]) for _ in range(n)],
    }
    return pd.DataFrame(data)

df = generate_diabetes_data()
df.to_csv("../logistic_regression_project/data.csv", index=False)
