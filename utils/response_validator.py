def validate_status_code(response, expected_code):
    assert response.status_code == expected_code, (
        f"Expected status {expected_code}, got {response.status_code}"
    )


def validate_key_in_response(response, key):
    response_json = response.json()
    assert key in response_json, (
        f"Key '{key}' not found in response: {response_json}"
    )


def validate_json_value(response, key, expected_value):
    response_json = response.json()
    actual_value = response_json.get(key)

    assert actual_value == expected_value, (
        f"Expected {key} = {expected_value}, got {actual_value}"
    )