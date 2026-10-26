import allure
import pytest

pytestmark = pytest.mark.api


@allure.feature("Booking API")
@allure.story("Negative")
def test_get_not_existing_booking(api):
    response = api.get_booking(999999999)

    assert response.status_code == 404


@allure.feature("Booking API")
@allure.story("Negative")
def test_update_without_token(api, booking_id, new_booking):
    response = api.update_booking(booking_id, new_booking)

    assert response.status_code == 403


@allure.feature("Booking API")
@allure.story("Negative")
def test_delete_without_token(api, booking_id):
    response = api.delete_booking(booking_id)

    assert response.status_code == 403


@allure.feature("Booking API")
@allure.story("Negative")
@pytest.mark.xfail(strict=True, reason="Known bug: API returns 500 instead of 400")
def test_create_booking_without_required_fields(api):
    # strict=True: when the API is fixed this XPASS turns the run red, so the xfail marker gets removed
    response = api.create_booking({"firstname": "Denys"})

    assert response.status_code == 400
