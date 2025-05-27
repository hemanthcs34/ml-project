import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(BASE, "data.csv"))

vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
X = vectorizer.fit_transform(df["Message"])
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

def detect_spam(message):
    vec = vectorizer.transform([message])
    pred = model.predict(vec)[0]
    return "not spam" if pred == "Ham" else "spam"
