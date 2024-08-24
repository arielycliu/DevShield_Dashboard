from flask import request, jsonify
from config import app, db
from models import Person


@app.route("/data", methods=["GET"])
def get_data():
    data = Person.query.all()
    json_data = list(map(lambda x: x.to_json(), data))
    return jsonify({"data": json_data})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
