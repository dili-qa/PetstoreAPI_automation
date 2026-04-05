import os
PROJECT_NAME = "Petstore API Automation"
BASE_URL = "https://reqres.in/api"

# Environment (can extend later)
ENV = os.getenv("ENV", "qa")

# Default headers

HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": os.getenv("API_KEY", "reqres-free-v1")
}
# Timeout
TIMEOUT = 10
