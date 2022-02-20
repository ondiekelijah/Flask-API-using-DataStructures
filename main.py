from flask import Flask, jsonify, request
import config


app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)

# Seeding to create default users

users = {
    1: {"fname": "John", "lname": "Doe", "username": "John96", "dob": "08/12/2000"},
    2: {
        "fname": "Mike",
        "lname": "Spencer",
        "username": "miker5",
        "dob": "01/08/2004",
    },
}


# Create a new user
@app.route("/user", methods=["POST"])
def create_user():

    data = request.get_json()

    if data["id"] not in users.keys():
        users[data["id"]] = {
            "fname": data["fname"],
            "lname": data["lname"],
            "username": data["username"],
            "dob": data["dob"],
        }
    else:
        return jsonify({"message": "user already exists"}), 401

    return jsonify({"message": "user created"}), 201


@app.route("/users", methods=["GET"])
def get_users():

    all_users = []

    for key in users:
        all_users.append(users[key])
        users[key]["id"] = key

    all_users.sort(key=lambda x: x["id"], reverse=True)

    return jsonify(all_users), 200


@app.route("/users/login", methods=["POST"])
def login_user():

    data = request.get_json()

    id = data["id"]
    username = data["username"]

    if id in users.keys():
        if users[id]["username"] == username:
            return jsonify(f"Welcome, you are logged in as {username}"), 200

    return jsonify("Invalid login credentials"), 401


if __name__ == "__main__":
    app.run(debug=True)
