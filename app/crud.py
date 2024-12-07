from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models import User


async def create_user(db: AsyncSession, name: str, email: str):
    user = User(name=name, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users


async def update_user(db: AsyncSession, user_id: int, name: str, email: str):
    stmt = select(User).filter(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        user.name = name
        user.email = email
        await db.commit()
        await db.refresh(user)

    return user


async def delete_user(db: AsyncSession, user_id: int):
    stmt = select(User).filter(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if user:
        await db.delete(user)
        await db.commit()

    return user
