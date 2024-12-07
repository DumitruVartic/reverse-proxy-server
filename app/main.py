from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
from app.models import SessionLocal, User

# Initialize the FastAPI app
app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User)
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, name, email)
    return db_user


@app.get("/users/", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, name: str, email: str, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user_id, name, email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
