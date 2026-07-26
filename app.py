from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os

app = Flask(__name__)
CORS(app)

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority")

def get_collection():
    client = MongoClient(MONGO_URI)
    return client["flask_assignment"]["students"]


@app.route("/submit", methods=["POST"])
def submit():
    try:
        data = request.get_json()
        name   = data.get("name")
        course = data.get("course")
        marks  = data.get("marks")

        if not name or not course or not marks:
            return jsonify({"success": False, "error": "All fields are required"}), 400

        student = {"name": name, "course": course, "marks": int(marks)}
        get_collection().insert_one(student)

        return jsonify({"success": True, "message": "Data submitted successfully"}), 200

    except PyMongoError as e:
        return jsonify({"success": False, "error": str(e)}), 500
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Flask backend is running"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
