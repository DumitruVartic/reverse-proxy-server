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

# Copy the wait_for_db.sh script into the container
COPY wait_for_db.sh /app/wait_for_db.sh
RUN chmod +x /app/wait_for_db.sh

# Expose the FastAPI port
EXPOSE 8000

# Command to run the wait_for_db.sh script before starting FastAPI
CMD /app/wait_for_db.sh && uvicorn main:app --host 0.0.0.0 --port 8000 --reload
