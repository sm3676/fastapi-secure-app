from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic import BaseModel, field_validator
from enum import Enum
from typing import Optional


class CalcType(str, Enum):
    Add = "Add"
    Sub = "Sub"
    Multiply = "Multiply"
    Divide = "Divide"


class CalculationCreate(BaseModel):
    a: float
    b: float
    type: CalcType

from pydantic import model_validator

class CalculationCreate(BaseModel):
    a: float
    b: float
    type: CalcType

    @model_validator(mode="after")
    def validate_division(self):
        if self.type == "Divide" and self.b == 0:
            raise ValueError("Division by zero not allowed")
        return self


class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: CalcType
    result: Optional[float]

from pydantic import ConfigDict

model_config = ConfigDict(from_attributes=True)
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