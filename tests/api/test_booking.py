<<<<<<< HEAD
import allure
=======
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
import pytest

pytestmark = pytest.mark.api


<<<<<<< HEAD
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
=======
@pytest.mark.smoke
def test_create_booking(booking_client, booking_payload):
    resp = booking_client.create_booking(booking_payload)
    assert resp.status_code == 200
    body = resp.json()
    assert isinstance(body["bookingid"], int)
    assert body["booking"] == booking_payload


def test_get_booking(booking_client, created_booking, booking_payload):
    resp = booking_client.get_booking(created_booking)
    assert resp.status_code == 200
    assert resp.json()["firstname"] == booking_payload["firstname"]


def test_update_booking_with_auth(auth_client, created_booking, booking_payload):
    updated = {**booking_payload, "totalprice": 999}
    resp = auth_client.update_booking(created_booking, updated)
    assert resp.status_code == 200
    assert resp.json()["totalprice"] == 999


def test_update_booking_without_auth_is_forbidden(booking_client, created_booking, booking_payload):
    resp = booking_client.update_booking(created_booking, booking_payload)
    assert resp.status_code == 403


def test_delete_booking(auth_client, booking_client, booking_payload):
    booking_id = booking_client.create_booking(booking_payload).json()["bookingid"]
    assert auth_client.delete_booking(booking_id).status_code == 201
    assert booking_client.get_booking(booking_id).status_code == 404
>>>>>>> a77e642a0b792e83b3c58612be5bdd1e9dd465f7
