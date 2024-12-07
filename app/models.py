from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database Configuration
DATABASE_URL = "postgresql+asyncpg://postgres:password@postgres_primary/datawarehouse"

# Async SQLAlchemy Engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Async Session Factory
SessionLocal = sessionmaker(engine, class_=AsyncSession, autocommit=False, autoflush=False)

# Declarative Base
Base = declarative_base()


# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)


# Database Session Dependency
async def get_db():
    async with SessionLocal() as db:
        yield db
