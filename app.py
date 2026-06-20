from pdf_report import generate_report
from flask import Flask, render_template, request
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# Load dataset
data = pd.read_csv("disease_data.csv")

X = data[["Fever", "Cough", "Headache", "Fatigue", "BodyPain", "SoreThroat"]]
y = data["Disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Disease information
disease_info = {
    "Flu": {
        "description": "A common viral infection affecting the respiratory system.",
        "precautions": [
            "Drink plenty of water",
            "Take adequate rest",
            "Eat healthy food"
        ]
    },
    "Cold": {
        "description": "A mild viral infection affecting the nose and throat.",
        "precautions": [
            "Drink warm fluids",
            "Take sufficient rest",
            "Avoid cold foods"
        ]
    },
    "Dengue": {
        "description": "A mosquito-borne viral disease causing fever and body pain.",
        "precautions": [
            "Stay hydrated",
            "Avoid mosquito exposure",
            "Consult a doctor immediately"
        ]
    },
    "Migraine": {
        "description": "A neurological condition causing severe headaches.",
        "precautions": [
            "Rest in a quiet room",
            "Stay hydrated",
            "Avoid stress"
        ]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    patient_name = request.form["patient_name"]
    age = request.form["age"]
    gender = request.form["gender"]

    fever = int(request.form["fever"])
    cough = int(request.form["cough"])
    headache = int(request.form["headache"])
    fatigue = int(request.form["fatigue"])
    bodypain = int(request.form["bodypain"])
    sorethroat = int(request.form["sorethroat"])

    result = model.predict(
        [[fever, cough, headache, fatigue, bodypain, sorethroat]]
    )[0]

    generate_report(
        patient_name,
        age,
        gender,
        result,
        disease_info[result]["description"],
        disease_info[result]["precautions"]
    )

    return render_template(
        "index.html",
        prediction=result,
        description=disease_info[result]["description"],
        precautions=disease_info[result]["precautions"],
        patient_name=patient_name,
        age=age,
        gender=gender
    )

if __name__ == "__main__":
    app.run(debug=True)