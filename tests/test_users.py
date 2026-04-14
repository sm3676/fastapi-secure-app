from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

def test_create_user():
    unique_id = str(uuid.uuid4())

    response = client.post("/users", json={
        "username": f"user_{unique_id}",
        "email": f"{unique_id}@example.com",
        "password": "123456"
    })

    assert response.status_code == 200