import pytest, requests, json
from main import app
import config


@pytest.fixture
def client():
    app.config.from_object(config.TestingConfig)
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_create_user(client):

    response = client.post(
        "/user",
        json={
            "id": 4,
            "fname": "James",
            "lname": "Max",
            "username": "Maxy",
            "dob": "08/12/2000",
        },
    )

    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 201


def test_fetch_users(client):

    response = client.get("/users")

    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200


def test_login_user(client):

    response = client.post("/users/login", json={"id": 1, "username": "John96"})

    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 200
    assert b"Welcome, you are logged in as John96" in response.data


def test_login_invalid(client):

    response = client.post("/users/login", json={"id": 454, "username": "miko98"})

    assert response.headers["Content-Type"] == "application/json"
    assert response.status_code == 401
    assert b"Invalid login credentials" in response.data
    assert b"Welcome, you are logged in as miko98" not in response.data
