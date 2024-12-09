import pytest
from crud import create_user, delete_user, get_users, update_user
from models import User
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/test_db"


@pytest.fixture(scope="module")
async def db_session():
    engine = create_async_engine(DATABASE_URL, echo=True, future=True)
    SessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False)

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.create_all)

    # Create session
    async with SessionLocal() as session:
        yield session

    # Clean up
    async with engine.begin() as conn:
        await conn.run_sync(User.metadata.drop_all)


@pytest.mark.asyncio
async def test_create_user(db_session: AsyncSession):
    user = await create_user(db_session, "John Doe", "john.doe@example.com")
    assert user.name == "John Doe"
    assert user.email == "john.doe@example.com"


@pytest.mark.asyncio
async def test_get_users(db_session: AsyncSession):
    await create_user(db_session, "Jane Doe", "jane.doe@example.com")
    users = await get_users(db_session)
    assert len(users) > 0


@pytest.mark.asyncio
async def test_update_user(db_session: AsyncSession):
    user = await create_user(db_session, "Mike", "mike@example.com")
    updated_user = await update_user(db_session, user.id, "Mike Updated", "mike.updated@example.com")
    assert updated_user.name == "Mike Updated"
    assert updated_user.email == "mike.updated@example.com"


@pytest.mark.asyncio
async def test_delete_user(db_session: AsyncSession):
    user = await create_user(db_session, "Delete Me", "delete@example.com")
    deleted_user = await delete_user(db_session, user.id)
    assert deleted_user.name == "Delete Me"
    assert deleted_user.email == "delete@example.com"
