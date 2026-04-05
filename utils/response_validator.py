def validate_status_code(response, expected):
    assert response.status_code == expected