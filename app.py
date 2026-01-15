from flask import Flask, request, jsonify
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

if __name__ == "__main__":
    app.run(debug=True)
