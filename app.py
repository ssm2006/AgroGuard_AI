from flask import Flask, request, jsonify, render_template
import os
import random

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🧠 Dummy AI + Knowledge Base
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

# -------------------- PAGE ROUTES --------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/predict")
def predict():
    return render_template("predict.html")

@app.route("/disease")
def disease():
    return render_template("disease.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/how-it-works")
def how_it_works():
    return render_template("how-it-works.html")

# -------------------- AI API ROUTE --------------------

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["image"]
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)

    disease, info = dummy_ai_prediction()

    return jsonify({
        "disease": disease,
        "confidence": info["confidence"],
        "severity": info["severity"],
        "symptoms": info["symptoms"],
        "prevention": info["prevention"],
        "treatment": info["treatment"]
    })

# -------------------- RUN --------------------

if __name__ == "__main__":
    app.run(debug=True)
