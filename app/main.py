from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import SessionLocal
from app.auth import hash_password

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pw = hash_password(user.password)

    db_user = models.User(
        username=user.username,
        email=user.email,
        password_hash=hashed_pw
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)