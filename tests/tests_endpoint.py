import pytest
from app import app
from flask import Flask


@pytest.fixture
def client():

    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, World!"


def test_hello_jose(client):
    response = client.get("/jose")
    assert response.status_code == 200
    assert response.data == b"Hello, Jose!"


def test_hello_coop(client):
    response = client.get("/coop")
    assert response.status_code == 200
    assert response.data == b"Hello, Coop!"


def test_hello_andrea(client):
    response = client.get("/andrea")
    assert response.status_code == 200
    assert response.data == b"Hello, Andrea!"
