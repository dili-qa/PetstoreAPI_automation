import os

BASE_URL = "https://reqres.in/api"

# Environment (can extend later)
ENV = os.getenv("ENV", "qa")

# Default headers
HEADERS = {
    "Content-Type": "application/json"
}

# Timeout
TIMEOUT = 10