from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import linked_list


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_Pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

db = SQLAlchemy(app)
now = datetime.now()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique = True, nullable=False)
    dob = db.Column(db.String(50), unique = True, nullable=False)
    posts = db.relationship("Post")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique = True, nullable=False)
    content = db.Column(db.Text,nullable=False)
    date =db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)




# Create a new user
@app.route("/user", methods=['POST'])
def create_user():

    data = request.get_json()
    new_user = User(
        fname = data["fname"],
        lname = data["lname"],
        username = data["username"],
        dob = data["dob"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "user created"}), 200

@app.route("/user/descending_id", methods=['GET'])
def get_all_users_descending():
    pass

@app.route("/user/ascending_id", methods=['GET'])
def get_all_users_ascending():
    pass

@app.route("/user/<user_id>", methods=['GET'])
def get_user(user_id):
    pass

@app.route("/user/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    pass

@app.route("/blog_post/<user_id>", methods=['POST'])
def create_blog_post(user_id):
    pass

@app.route("/user/<user_id>", methods=['GET'])
def get_all_blog_posts(user_id):
    pass


@app.route("/blog_post/<blog_post_id>", methods=['GET'])
def get_one_blog_post(blog_post_id):
    pass


@app.route("/blog_post/<blog_post_id>", methods=['DELETE'])
def delete_blog_post(blog_post_id):
    pass


if __name__ == "__main__":
    app.run(debug=True)
