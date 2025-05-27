import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("knn_project/data.csv")
X = df.drop(columns=["Label"])
le = LabelEncoder()
y = le.fit_transform(df["Label"])
model = KNeighborsClassifier(n_neighbors=3).fit(X, y)

def classify_voice(features):
    lbl = model.predict([features])[0]
    return le.inverse_transform([lbl])[0]
