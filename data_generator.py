from random import randrange
from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from faker import Faker
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import server

# app
app = Flask(__name__)

# config
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)
faker = Faker()

# create dummy users
for i in range(10):
    fname = faker.first_name()
    lname = faker.last_name()
    username = faker.user_name()
    dob = faker.date()

    new_user = server.User(fname=fname, lname=lname, username=username, dob=dob)

    db.session.add(new_user)
    db.session.commit()

# create dummy blog posts
for i in range(10):
    title = faker.sentence(5)
    content = faker.paragraph(190)
    date = faker.date_time()
    user_id = randrange(1, 10)

    new_blog_post = server.Post(
        title=title, content=content, date=date, user_id=user_id
    )
    db.session.add(new_blog_post)
    db.session.commit()
