from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load model and encoder
model = joblib.load("model.joblib")
dv = joblib.load("dv.joblib")

# 👉 This route is missing in your file; add it!
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        X = dv.transform([data])
        y_pred = model.predict(X)[0]

        return jsonify({"predicted_price": round(float(y_pred), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=9696)
