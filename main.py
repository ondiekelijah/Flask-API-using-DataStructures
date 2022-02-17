from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import utils, config



app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    dob = db.Column(db.String(50), nullable=False)


# Create a new user
@app.route("/user", methods=["POST"])
def create_user():

    data = request.get_json()
    new_user = User(
        fname=data["fname"],
        lname=data["lname"],
        username=data["username"],
        dob=data["dob"],
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user created"}), 200


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    all_users_ll = utils.LinkedList()

    for user in users:
        all_users_ll.insert_data(
            {
                "id": user.id,
                "fname": user.fname,
                "lname": user.lname,
                "username": user.username,
                "dob": user.dob,
            }
        )
    return jsonify(all_users_ll.to_list()), 200


@app.route("/users/login", methods=["POST"])
def login_user():

    data = request.get_json()

    id = data["id"]
    username = data["username"]

    users = User.query.all()
    all_users_ll = utils.LinkedList()

    for user in users:
        all_users_ll.insert_data(
            {
                "id": user.id,
                "fname": user.fname,
                "lname": user.lname,
                "username": user.username,
                "dob": user.dob,
            }
        )

    user = all_users_ll.login_user(user_id=id, username=username)

    return jsonify(user), 200


if __name__ == "__main__":
    app.run(debug=True)
