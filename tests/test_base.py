from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/api/base/ping")
    assert response.status_code == 200
    assert response.json() == {'result': 'pong'}
