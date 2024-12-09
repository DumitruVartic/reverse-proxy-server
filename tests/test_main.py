from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.models import Base

DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/test_db"

client = TestClient(app)


def setup_module():
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_user():
    response = client.post("/users/", json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
    assert response.json()["email"] == "alice@example.com"


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_update_user():
    user_data = {"name": "Bob", "email": "bob@example.com"}
    response = client.post("/users/", json=user_data)
    user_id = response.json()["id"]

    updated_data = {"name": "Bob Updated", "email": "bob.updated@example.com"}
    response = client.put(f"/users/{user_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Bob Updated"


def test_delete_user():
    user_data = {"name": "Charlie", "email": "charlie@example.com"}
    response = client.post("/users/", json=user_data)
    user_id = response.json()["id"]

    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Charlie"
