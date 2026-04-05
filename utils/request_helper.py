import requests
from utils.logger import get_logger
from config import BASE_URL, HEADERS, TIMEOUT

logger = get_logger("API")


def get_request(endpoint, headers=None):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"GET → {url}")

    response = requests.get(
        url,
        headers=headers or HEADERS,
        timeout=TIMEOUT
    )

    logger.info(f"Response [{response.status_code}] → {response.text}")
    return response


def post_request(endpoint, payload=None, headers=None):
    url = f"{BASE_URL}{endpoint}"
    logger.info(f"POST → {url}")
    logger.info(f"Payload → {payload}")

    response = requests.post(
        url,
        json=payload,
        headers=headers or HEADERS,
        timeout=TIMEOUT
    )

    logger.info(f"Response [{response.status_code}] → {response.text}")
    return response