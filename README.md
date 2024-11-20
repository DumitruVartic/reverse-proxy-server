# reverse-proxy-server

Implementation of a Reverse Proxy Server developed as part of the Distributed Applications Programming course. It should direct client requests to backend data warehouses, using load balancing to evenly distribute requests and caching to speed up responses by storing frequently used data.

## Prerequisites

- Python 3.x
- Docker and Docker Compose

## Setup

```bash
git clone https://github.com/DumitruVartic/reverse-proxy-server.git
cd reverse-proxy-server
pip install -r requirements.txt
pre-commit install
```
