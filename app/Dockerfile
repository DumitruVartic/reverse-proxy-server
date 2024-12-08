FROM python:3.10-slim

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container at /app
COPY . /app/

# Command to run the wait_for_db.sh script before starting FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
