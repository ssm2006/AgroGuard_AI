from flask import Flask, request, jsonify, send_from_directory
import os
import random
import threading

# 🔹 Weather module import
from weather_module import auto_weather_update

app = Flask(__name__, static_folder="static")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -------------------------------
# Upload Folder
# -------------------------------
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -------------------------------
# 🧠 Dummy AI Database
# -------------------------------
DISEASE_DB = {
    "Bacterial Blight": {
        "confidence": 94,
        "severity": "High",
        "symptoms": "Angular leaf spots, vein blackening, leaf drying",
        "prevention": "Use certified seeds, crop rotation, avoid water stagnation",
        "treatment": "Copper-based fungicide spray"
    },
    "Leaf Curl Virus": {
        "confidence": 89,
        "severity": "Very High",
        "symptoms": "Leaf curling, yellow mosaic pattern, stunted growth",
        "prevention": "Control whiteflies, use resistant varieties",
        "treatment": "Imidacloprid or neem oil spray"
    },
    "Fungal Infection": {
        "confidence": 86,
        "severity": "Medium",
        "symptoms": "Brown circular spots, leaf wilting",
        "prevention": "Avoid excess moisture, proper spacing",
        "treatment": "Mancozeb or Carbendazim fungicide"
    },
    "Healthy": {
        "confidence": 98,
        "severity": "None",
        "symptoms": "No disease detected",
        "prevention": "Maintain soil nutrients and irrigation",
        "treatment": "No treatment required"
    }
}

def dummy_ai_prediction():
    disease = random.choice(list(DISEASE_DB.keys()))
    return disease, DISEASE_DB[disease]

# -------------------------------
# 🌦 Weather Background Thread
# -------------------------------
weather_thread = threading.Thread(
    target=auto_weather_update,
    args=("Pune",),
    daemon=True
)
weather_thread.start()
print("Weather module running in background...")

# -------------------------------
# 🌐 Page Routes (HTML in ROOT)
# -------------------------------
@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/about")
def about():
    return send_from_directory(BASE_DIR, "about.html")

@app.route("/dashboard")
def dashboard():
    return send_from_directory(BASE_DIR, "dashboard.html")

@app.route("/how-it-works")
def how_it_works():
    return send_from_directory(BASE_DIR, "how-it-works.html")

@app.route("/disease")
def disease():
    return send_from_directory(BASE_DIR, "disease.html")

@app.route("/predict")
def predict():
    return send_from_directory(BASE_DIR, "predict.html")

@app.route("/login")
def login():
    return send_from_directory(BASE_DIR, "login.html")

# -------------------------------
# 🌿 Disease Detection API
# -------------------------------
@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["image"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    disease, info = dummy_ai_prediction()

    return jsonify({
        "disease": disease,
        "confidence": info["confidence"],
        "severity": info["severity"],
        "symptoms": info["symptoms"],
        "prevention": info["prevention"],
        "treatment": info["treatment"]
    })

# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
