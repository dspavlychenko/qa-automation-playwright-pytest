import pytest

pytestmark = pytest.mark.api


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
