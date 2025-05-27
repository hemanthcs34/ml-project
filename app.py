from flask import Flask, render_template, request
from linear_regression_project.model import predict_energy
from logistic_regression_project.model import predict_diabetes
from knn_project.model import classify_voice
from naive_bayes_project.model import detect_spam

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/linear", methods=["GET", "POST"])
def linear():
    if request.method == "POST":
        hour = float(request.form["hour"])
        temp = float(request.form["temp"])
        pred = predict_energy(hour, temp)
        return render_template("linear_result.html", hour=hour, temp=temp, prediction=round(pred,2))
    return render_template("linear.html")

@app.route("/logistic", methods=["GET", "POST"])
def logistic():
    if request.method == "POST":
        inputs = {k: float(request.form[k]) for k in ["Glucose","BloodPressure","BMI","Age","Insulin"]}
        pred = predict_diabetes(inputs)
        return render_template("logistic_result.html", prediction=pred)
    return render_template("logistic.html")

@app.route("/knn", methods=["GET", "POST"])
def knn():
    if request.method == "POST":
        features = [float(request.form[k]) for k in ["MeanFreq","SD","Median","IQR","Skew","Kurt"]]
        label = classify_voice(features)
        return render_template("knn_result.html", result=label)
    return render_template("knn.html")

@app.route("/naive", methods=["GET", "POST"])
def naive():
    if request.method == "POST":
        msg = request.form["message"]
        label = detect_spam(msg)
        return render_template("naive_result.html", result=label)
    return render_template("naive.html")

if __name__ == "__main__":
    app.run(debug=True)
