import allure
import pytest

from config.settings import API_PASSWORD, API_USER

pytestmark = pytest.mark.api


@allure.feature("Auth API")
@pytest.mark.smoke
def test_api_is_alive(api):
    response = api.ping()

    assert response.status_code == 201


@allure.feature("Auth API")
def test_get_token(api):
    response = api.create_token(API_USER, API_PASSWORD)

    assert response.status_code == 200
    assert "token" in response.json()


@allure.feature("Auth API")
def test_get_token_wrong_password(api):
    response = api.create_token(API_USER, "wrong")

    # Quirk of Restful-Booker: bad credentials still answer 200 with a "reason" instead of 401,
    # so the body is the only reliable signal here.
    assert response.json()["reason"] == "Bad credentials"
    assert "token" not in response.json()
