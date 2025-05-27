import pandas as pd
from sklearn.linear_model import LinearRegression
import os

BASE = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(BASE, "data.csv"))

X = df[["hour", "temp"]]
y = df["energy"]
model = LinearRegression().fit(X, y)

def predict_energy(hour, temp):
    return float(model.predict([[hour, temp]])[0])
