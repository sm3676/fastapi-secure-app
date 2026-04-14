# 🚀 FastAPI Secure User Management App

This project is a secure FastAPI-based web application that allows users to be created with proper validation, password hashing, testing, and Docker deployment.

---

## 📌 Features

- ✅ FastAPI REST API
- ✅ User creation endpoint (`POST /users`)
- ✅ Password hashing for security
- ✅ Input validation using Pydantic
- ✅ Unit testing with pytest
- ✅ CI/CD pipeline using GitHub Actions
- ✅ Docker containerization
- ✅ Docker Hub image deployment

---

## 🛠️ Tech Stack

- FastAPI
- Python 3.12+
- SQLAlchemy
- SQLite
- Pytest
- Docker
- GitHub Actions

---

## 📂 Project Structure
fastapi-secure-app/
│── app/
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ └── auth.py
│
│── tests/
│ ├── test_auth.py
│ └── test_users.py
│
│── Dockerfile
│── requirements.txt
│── README.md


---

## ▶️ How to Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt

2. Run FastAPI app

uvicorn app.main:app --reload

3. Open in browser

http://localhost:8000/docs

🧪 Running Tests
pytest

🐳 Docker Setup

1. Build Docker image
docker build -t fastapi-app .

2. Run container

docker run -d -p 8000:8000 fastapi-app

3. Access API

http://localhost:8000/docs

☁️ Docker Hub

https://hub.docker.com/r/sm3676/fastapi-user-assignment

🔄 CI/CD Pipeline
Implemented using GitHub Actions
Automatically runs tests on push
Ensures code quality and reliability

👩‍💻 Author

Sharvani Rao