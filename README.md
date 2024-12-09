# reverse-proxy-server

Implementation of a Reverse Proxy Server developed as part of the Distributed Applications Programming course. It should direct client requests to backend data warehouses, using load balancing to evenly distribute requests and caching to speed up responses by storing frequently used data.

## Usage

If all prerequisites are met and everything is set up correctly, you can start the server by running:

## Important ! if something not working, try to run the following commands

```bash
# Stop all running containers
docker stop $(docker ps -aq)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q) -f

# Run the server
docker-compose up --build --scale api=5
```

Clone the repository:

```bash
git clone https://github.com/DumitruVartic/reverse-proxy-server.git
cd reverse-proxy-server
docker-compose up --build --scale api=5 # or any number of instances
```

### Also look at the **Swagger UI** for testing the API

API documentation is available at <http://localhost:8080/docs>

## Prerequisites

- Python 3.x
- Docker and Docker Compose
- Nginx Look at the [Nginx setup](#nginx-setup) section for more details.
- PostgreSQL Look at the [Database setup](#database-setup) section for more details.

Install the required packages:

```bash
pip install -r requirements.txt
```

## Setup

```bash
git clone https://github.com/DumitruVartic/reverse-proxy-server.git
cd reverse-proxy-server
```

### Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate # Linux and MacOS
# or
.venv\Scripts\activate # Windows
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Precommit code checker (optional)

```bash
pre-commit install
```

## Database setup

Install PostgreSQL on your system.
After installation, start the PostgreSQL service. And run `setup_db.py` to create the necessary tables.

Arch linux:

```bash
sudo pacman -S postgresql
sudo systemctl enable postgresql.service
sudo systemctl start postgresql.service
```

Initialize the database cluster (run only once):

```bash
sudo -iu postgres initdb --locale=en_US.UTF-8 -D /var/lib/postgres/data
sudo systemctl start postgresql
sudo systemctl enable postgresql.service
```

If second time you run the command and get error, run this and then again the above command:

```bash
sudo rm -rf /var/lib/postgres/data
```

MacOS:

```bash
brew install postgresql
brew services start postgresql
```

Windows:
Install PostgreSQL from the official website:
[PostgreSQL](https://www.postgresql.org/download/windows/)
Start the PostgreSQL server via the installed utility.

## Nginx setup

Arch linux:

```bash
sudo pacman -S nginx
sudo systemctl enable nginx.service
sudo systemctl start nginx.service
```

MacOS:

```bash
brew install nginx
brew services start nginx
```

Windows:
Install Nginx from the official website:
[Nginx](https://nginx.org/en/download.html)
