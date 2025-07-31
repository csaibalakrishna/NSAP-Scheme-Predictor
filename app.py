from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__, template_folder="templates")
CORS(app)

# 🔐 IBM Cloud Credentials - HARDCODED for now (replace with os.getenv later)
API_KEY = "4iRD3jeiJkvG1Vh_8m8PMTsZUFf2ecbIroQExE2R0SiK"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/c6818797-652c-4391-9842-f8cbf84afd2a/predictions?version=2021-05-01"

# 🌐 Basic route
@app.route("/")
def home():
    return render_template("index.html")

# 🔐 IBM IAM Token Generation
def get_token():
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "apikey": API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code != 200:
        print("❌ Token request failed:", response.status_code)
        print("❌ Response body:", response.text)
        return None

    token = response.json().get("access_token")
    print("✅ Access token acquired.")
    return token

# 🧠 Predict Route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        fields = [
            "finyear", "lgdstatecode", "statename", "lgddistrictcode", "districtname",
            "totalbeneficiaries", "totalmale", "totalfemale", "totaltransgender",
            "totalsc", "totalst", "totalgen", "totalobc", "totalaadhaar", "totalmobilenumber"
        ]

        # Validate inputs
        if not all(field in data for field in fields):
            return jsonify({"error": "Missing one or more required fields."}), 400

        # Format the request
        values = [[data[field] for field in fields]]
        payload = {"input_data": [{"fields": fields, "values": values}]}
        print("📤 Sending payload:", payload)

        # Get token
        token = get_token()
        if not token:
            return jsonify({"error": "Failed to obtain access token"}), 401

        headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json"
        }

        # Request prediction
        response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)

        print("📥 IBM Response Code:", response.status_code)
        print("📥 IBM Response Body:", response.text)

        if response.status_code != 200:
            return jsonify({"error": "Prediction failed", "details": response.text}), 500

        response_json = response.json()
        prediction = response_json["predictions"][0]["values"][0][0]

        return jsonify({"prediction": prediction})

    except Exception as e:
        print("🔥 Internal Server Error:", str(e))
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# 🚀 Run App
if __name__ == "__main__":
    app.run(debug=True)
