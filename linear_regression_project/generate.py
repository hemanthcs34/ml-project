import pandas as pd
import numpy as np

np.random.seed(42)

data = []
for i in range(200):
    hour = np.random.randint(0, 24)
    temp = np.random.uniform(10, 35)  
    energy = 50 + (hour * 5) + (temp * 3) + np.random.normal(0, 10)
    data.append([hour, round(temp,2), round(energy,2)])

df = pd.DataFrame(data, columns=["hour", "temp", "energy"])
df.to_csv("../linear_regression_project/data.csv", index=False)

print(df.head())
