from flask import request, jsonify
from config import app, db
from models import HoursByType, MeetingCost, Person, ProductiveHours

@app.route("/hours_by_type", methods=["GET"])
def get_hours_by_type():
    data = HoursByType.query.all()
    json_data = list(map(lambda x: x.to_json(), data))
    return jsonify({"data": json_data})

@app.route("/meeting_cost", methods=["GET"])
def get_meeting_cost():
    data = MeetingCost.query.all()
    json_data = list(map(lambda x: x.to_json(), data))
    return jsonify({"data": json_data})

@app.route("/person", methods=["GET"])
def get_person():
    data = Person.query.all()
    json_data = list(map(lambda x: x.to_json(), data))
    return jsonify({"data": json_data})

@app.route("/productive_hours", methods=["GET"])
def get_productive_hours():
    data = ProductiveHours.query.all()
    json_data = list(map(lambda x: x.to_json(), data))
    return jsonify({"data": json_data})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
