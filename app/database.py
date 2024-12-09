from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This should be in the .env file
DATABASE_URL = "postgresql+asyncpg://postgres:password@postgres:5432/datawarehouse"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False)

Base = declarative_base()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db():
    async with SessionLocal() as db:
        yield db
