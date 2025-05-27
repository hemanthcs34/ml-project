import os
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

BASE = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(BASE, "data.csv"))
vectorizer = CountVectorizer().fit(df["Message"])
X = vectorizer.transform(df["Message"])
y = df["Label"]
model = MultinomialNB().fit(X, y)

def detect_spam(message):
    vec = vectorizer.transform([message])
    pred = model.predict(vec)[0]
    return "true" if pred == "Ham" else "spam"
