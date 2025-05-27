import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("logistic_regression_project/data.csv")
X = df.drop(columns=["Outcome"])
y = df["Outcome"]
model = LogisticRegression(max_iter=500).fit(X, y)

def predict_diabetes(inputs):
    vals = [[inputs["Glucose"],inputs["BloodPressure"],inputs["BMI"],inputs["Age"],inputs["Insulin"]]]
    return int(model.predict(vals)[0])
