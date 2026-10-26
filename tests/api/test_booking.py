import allure
import pytest

pytestmark = pytest.mark.api


@allure.feature("Booking API")
@allure.story("Create")
@pytest.mark.smoke
def test_create_booking(api, admin_api, new_booking):
    response = api.create_booking(new_booking)

    assert response.status_code == 200
    created_id = response.json()["bookingid"]
    try:
        assert response.json()["booking"] == new_booking
    finally:
        admin_api.delete_booking(created_id)  # cleanup runs even if the assertion above fails


@allure.feature("Booking API")
@allure.story("Read")
def test_get_booking(api, booking_id, new_booking):
    response = api.get_booking(booking_id)

    assert response.status_code == 200
    assert response.json() == new_booking


@allure.feature("Booking API")
@allure.story("Read")
def test_get_all_booking_ids(api, booking_id):
    response = api.get_booking_ids()

    ids = [item["bookingid"] for item in response.json()]
    assert booking_id in ids


@allure.feature("Booking API")
@allure.story("Read")
def test_find_booking_by_name(api, booking_id):
    response = api.get_booking_ids(firstname="Denys", lastname="Tester")

    ids = [item["bookingid"] for item in response.json()]
    assert booking_id in ids


@allure.feature("Booking API")
@allure.story("Update")
def test_update_booking(admin_api, booking_id, new_booking):
    new_booking["totalprice"] = 999

    response = admin_api.update_booking(booking_id, new_booking)

    assert response.status_code == 200
    assert response.json()["totalprice"] == 999


@allure.feature("Booking API")
@allure.story("Update")
def test_update_booking_partially(admin_api, booking_id):
    response = admin_api.partial_update_booking(booking_id, {"firstname": "Ivan"})

    assert response.status_code == 200
    assert response.json()["firstname"] == "Ivan"
    assert response.json()["lastname"] == "Tester"  # other fields not changed


@allure.feature("Booking API")
@allure.story("Delete")
def test_delete_booking(api, admin_api, booking_id):
    # booking_id fixture also tries to delete it in teardown, so nothing leaks if an assertion fails
    response = admin_api.delete_booking(booking_id)

    assert response.status_code == 201
    assert api.get_booking(booking_id).status_code == 404
