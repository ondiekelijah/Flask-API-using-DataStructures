import pytest, requests, json
from main import app, db, User
import config


@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture()
def init_database():
    # Create the database and the database table
    db.create_all()

    # Insert test data
    test_user = User(fname="John", lname="Doe", username="John96", dob="08/12/2000")

    db.session.add(test_user)
    db.session.commit()

    yield db
    db.session.remove()
    db.drop_all()


def test_create_user(client, init_database):

    user = User(fname="Mike", lname="Spencer", username="miko98", dob="01/08/1990")
    db.session.add(user)
    db.session.commit()

    assert user.fname == "Mike"
    assert user.lname == "Spencer"
    assert user.username == "miko98"
    assert user.dob == "01/08/1990"


def test_fetch_users(client, init_database):

    response = client.get("/users")

    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200

    assert b"John" in response.data
    assert b"Doe" in response.data
    assert b"John96" in response.data
    assert b"08/12/2000" in response.data


def test_login_user(client, init_database):

    response = client.post("/users/login", json={"id": 1, "username": "John96"})

    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert b"Welcome, you are logged in as John96" in response.data


def test_login_invalid(client, init_database):

    response = client.post("/users/login", json={"id": 454, "username": "miko98"})

    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert b"Invalid login credentials" in response.data
    assert b"Welcome, you are logged in as miko98" not in response.data
