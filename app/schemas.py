from pydantic import BaseModel, EmailStr, ConfigDict

# 🔹 For creating user (REQUEST)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# 🔹 For returning user (RESPONSE)
class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)