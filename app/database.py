from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:yourpassword@postgres_primary/datawarehouse"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False)

Base = declarative_base()


async def get_db():
    async with SessionLocal() as db:
        yield db