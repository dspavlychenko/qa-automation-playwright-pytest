import pytest

pytestmark = pytest.mark.api

COUNTRY_QUERY = """
query Country($code: ID!) {
  country(code: $code) { name capital currency languages { name } }
}
"""


@pytest.mark.parametrize("code, name, capital", [("UA", "Ukraine", "Kyiv"), ("DE", "Germany", "Berlin")])
def test_get_country_by_code(graphql_client, code, name, capital):
    resp = graphql_client.query(COUNTRY_QUERY, {"code": code})
    assert resp.status_code == 200
    country = resp.json()["data"]["country"]
    assert country["name"] == name
    assert country["capital"] == capital


def test_unknown_country_returns_null(graphql_client):
    resp = graphql_client.query(COUNTRY_QUERY, {"code": "XX"})
    assert resp.json()["data"]["country"] is None


def test_invalid_query_returns_error(graphql_client):
    resp = graphql_client.query("{ country(code: \"UA\") { unknownField } }")
    assert "errors" in resp.json()
