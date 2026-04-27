"""
Testing Suite for the FastAPI Statistical Calculation web app

Objectives:
- Test accuracy of endpoints
- Test error handling
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_mean_valid():
    response = client.post("/mean", json={"numbers": [1, 2, 3, 4]})
    assert response.status_code == 200
    assert response.json() == {"mean": 2.5}


def test_stddev_valid():
    response = client.post("/stddev", json={"numbers": [1, 2, 3, 4]})
    assert response.status_code == 200
    # population stddev of [1,2,3,4] = ~1.118
    assert response.json() == {"stddev": 1.118}

def test_rounding():
    response = client.post("/mean", json={"numbers": [1, 2, 2]})
    assert response.json()["mean"] == 1.667


def test_empty_list():
    response = client.post("/mean", json={"numbers": []})
    assert response.status_code == 422  # validation error


def test_invalid_type():
    response = client.post("/mean", json={"numbers": ["a", "b"]})
    assert response.status_code == 422


def test_missing_field():
    response = client.post("/mean", json={})
    assert response.status_code == 422