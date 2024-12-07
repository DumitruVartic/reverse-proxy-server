import time

import psycopg2
from models import Base
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine

DB_NAME = "datawarehouse"
DB_USER = "postgres"
DB_PASSWORD = "password"
DB_HOST = "postgres_primary"
DB_PORT = 5432


def wait_for_db():
    """Wait for the database to be ready."""
    while True:
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT,
            )
            conn.close()
            print("Database is ready!")
            break
        except Exception:
            print("Waiting for database to be ready...")
            time.sleep(2)


def create_database():
    """Check and create the database if it doesn't exist."""
    wait_for_db()  # Wait for the database to be ready
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        # Check if the database exists
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname='{DB_NAME}';")
        if not cursor.fetchone():
            print(f"Creating database '{DB_NAME}'...")
            cursor.execute(f"CREATE DATABASE {DB_NAME};")
        else:
            print(f"Database '{DB_NAME}' already exists.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if "cursor" in locals():
            cursor.close()
        if "conn" in locals():
            conn.close()


def initialize_tables():
    """Initialize tables in the database."""
    print("Creating tables...")
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")


if __name__ == "__main__":
    create_database()
    initialize_tables()
