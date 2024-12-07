from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(UserCreate):
    id: int

    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy models as dictionaries
