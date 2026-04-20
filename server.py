from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    name = request.form.get('name')
    file = request.files.get('photo')

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        with open("data.csv", "a") as f:
            f.write(f"{name},{file.filename}\n")

        return "Upload successful"

    return "No file"

