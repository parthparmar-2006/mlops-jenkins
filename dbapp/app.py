from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///records.db"
db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float)
    sepal_width = db.Column(db.Float)
    petal_length = db.Column(db.Float)
    petal_width = db.Column(db.Float)
    prediction = db.Column(db.String(30))


with app.app_context():
    db.create_all()


@app.route("/add_record", methods=["POST"])
def add_record():
    data = request.get_json()
    db.session.add(Record(**data))
    db.session.commit()
    return jsonify({"status": "saved"})


@app.route("/records")
def records():
    rows = Record.query.order_by(Record.id.desc()).all()
    return jsonify([
        {"id": r.id, "sepal_length": r.sepal_length, "sepal_width": r.sepal_width,
         "petal_length": r.petal_length, "petal_width": r.petal_width,
         "prediction": r.prediction}
        for r in rows
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
