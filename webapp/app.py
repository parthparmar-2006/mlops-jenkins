import os
import pickle

import numpy as np
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

# dbapp is the docker compose service name (resolved by Docker's internal DNS)
DB_URL = os.getenv("DB_URL", "http://dbapp:8001")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    keys = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    values = [float(request.form[k]) for k in keys]
    prediction = model.predict(np.array([values]))[0]

    record = dict(zip(keys, values), prediction=prediction)
    requests.post(f"{DB_URL}/add_record", json=record, timeout=5)

    return render_template("index.html", prediction=prediction)


@app.route("/records")
def records():
    rows = requests.get(f"{DB_URL}/records", timeout=5).json()
    return render_template("display_records.html", records=rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
