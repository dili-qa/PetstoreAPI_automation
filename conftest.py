# Reserved for future pytest integration
# Currently not used actively (Behave handles execution)

import pytest


@pytest.fixture(scope="session")
def base_url():
    from config import BASE_URL
    return BASE_URL