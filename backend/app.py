from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
CORS(app)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route("/gemini-api", methods=["POST"])
def gemini_predict():
    data = request.json
    prompt = data["prompt"]
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({"prediction": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
