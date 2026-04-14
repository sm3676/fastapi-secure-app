from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "123456"
    })

    assert response.status_code == 200