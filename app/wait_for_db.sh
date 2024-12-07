#!/bin/bash

# Wait for PostgreSQL to be ready
until pg_isready -h postgres_primary -U postgres -d datawarehouse; do
  echo "Waiting for PostgreSQL to be ready..."
  sleep 2
done

# Once the database is ready, run the setup script
python setup_db.py
