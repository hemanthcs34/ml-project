import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("linear_regression_project/data.csv")
X = df[["Hour","Temperature"]]
y = df["Energy_kWh"]
model = LinearRegression().fit(X, y)

def predict_energy(hour, temp):
    return float(model.predict([[hour, temp]])[0])
