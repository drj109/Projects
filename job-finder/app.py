from pathlib import Path
from flask import Flask, jsonify, request
from model import JobIndex

app = Flask(__name__)
index = JobIndex(Path(__file__).with_name("jobs.csv"))


@app.get("/")
def home():
    return app.send_static_file("index.html")


@app.post("/api/matches")
def matches():
    data = request.get_json(silent=True)
    skills = data.get("skills") if isinstance(data, dict) else None
    if not isinstance(skills, str) or not 1 <= len(skills.strip()) <= 2000:
        return jsonify(error="Enter 1 to 2,000 characters describing your skills."), 400
    return jsonify(matches=index.search(skills.strip()))
