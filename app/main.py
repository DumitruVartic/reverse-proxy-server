from typing import List

import crud as crud
from database import get_db, init_db
from fastapi import Depends, FastAPI, HTTPException
from schemas import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.create_user(db, user.name, user.email)
    return db_user


@app.get("/users/", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await crud.get_users(db)
    return users


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud.update_user(db, user_id, user.name, user.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.delete("/users/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud.delete_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
