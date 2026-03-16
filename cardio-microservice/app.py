from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Cardiovascular prediction microservice running"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    age = data.get("age", 0)
    cholesterol = data.get("cholesterol", 0)
    smoke = data.get("smoke", 0)

    risk = 0

    if cholesterol > 1:
        risk += 1
    if smoke == 1:
        risk += 1
    if age > 18000:
        risk += 1

    prediction = 1 if risk >= 2 else 0

    return jsonify({
        "prediction": prediction,
        "risk_score": risk,
        "input": data
    })

app.run(host="0.0.0.0", port=8080)
